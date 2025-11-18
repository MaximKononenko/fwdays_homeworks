import pulumi
from pulumi import ResourceOptions
from pulumi_docker import Network, RemoteImage, Container

# Configuration
stack_name = pulumi.get_stack()


class WebAppStack(pulumi.ComponentResource):
    def __init__(self, name: str, port: int, opts: ResourceOptions | None = None):
        super().__init__("custom:resource:WebAppStack", name, {}, opts)

        parent_opts = ResourceOptions(parent=self)

        # Create Docker network
        network = Network(f"{name}-network",
                          name=f"webapp-network-{name}",
                          driver="bridge",
                          opts=parent_opts)

        # Redis image and container
        redis_image = RemoteImage(f"{name}-redis-image",
                                  name="redis:7-alpine",
                                  keep_locally=True,
                                  opts=parent_opts)

        redis_container = Container(f"{name}-redis",
                                    name=f"redis-{name}",
                                    image=redis_image.image_id,
                                    networks_advanced=[{"name": network.name, "aliases": ["redis"]}],
                                    ports=[{"internal": 6379, "external": port + 1000}],
                                    restart="unless-stopped",
                                    opts=parent_opts)
        # expose as component attributes
        self.redisContainer = redis_container

        # Nginx image and container
        nginx_image = RemoteImage(f"{name}-nginx-image",
                                  name="nginx:alpine",
                                  keep_locally=True,
                                  opts=parent_opts)

        nginx_config = r"""
events {
    worker_connections 1024;
}

http {
    upstream redis_backend {
        server redis:6379;
    }
    server {
        listen 80;
        location / {
            root /usr/share/nginx/html;
            index index.html;
        }
        location /health {
            access_log off;
            return 200 "healthy\n";
            add_header Content-Type text/plain;
        }
    }
}
"""

        index_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Pulumi Docker Demo - {name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
        .container {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .header {{ color: #2563eb; border-bottom: 2px solid #2563eb; padding-bottom: 10px; }}
        .info {{ margin: 20px 0; padding: 15px; background: #eff6ff; border-radius: 4px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1 class="header">🚀 Pulumi Docker Demo</h1>
        <div class="info">
            <h2>Stack: {name}</h2>
            <p><strong>Port:</strong> {port}</p>
            <p><strong>Redis Port:</strong> {port + 1000}</p>
            <p><strong>Status:</strong> ✅ Running</p>
        </div>
        <p>This Nginx server is running in a Docker container managed by Pulumi!</p>
        <p>Redis is available at: redis:6379 (internal network)</p>
        <p><a href="/health">Health Check</a></p>
    </div>
</body>
</html>
"""

        nginx_container = Container(f"{name}-nginx",
                                    name=f"nginx-{name}",
                                    image=nginx_image.image_id,
                                    networks_advanced=[{"name": network.name}],
                                    ports=[{"internal": 80, "external": port}],
                                    envs=[f"REDIS_HOST=redis", f"STACK_NAME={name}", f"PORT={port}"],
                                    uploads=[
                                        {"content": nginx_config, "file": "/etc/nginx/nginx.conf"},
                                        {"content": index_html, "file": "/usr/share/nginx/html/index.html"}
                                    ],
                                    restart="unless-stopped",
                                    opts=parent_opts)

        # expose as component attributes
        self.nginxContainer = nginx_container

        # Register outputs
        self.register_outputs({
            "nginxContainerId": nginx_container.id,
            "redisContainerId": redis_container.id,
            "networkId": network.id,
        })


# Instantiate the stack
port = 8080 if stack_name == "prod" else 8081
app = WebAppStack(stack_name, port)

pulumi.export('nginxUrl', pulumi.Output.concat('http://localhost:', str(port)))
pulumi.export('redisPort', port + 1000)
pulumi.export('stackInfo', {"name": stack_name, "nginxContainer": app.nginxContainer.name})

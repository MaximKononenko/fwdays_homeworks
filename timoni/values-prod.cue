// Production values for my-web-app

@if(!debug)

package main

values: {
	message: "Hello from Production"
	image: {
		repository: "nginx"
		digest:     ""
		tag:        "latest"
	}
	replicas: 3
	service: {
		port: 80
	}
	env: [
		{
			name:  "ENV"
			value: "production"
		},
		{
			name:  "LOG_LEVEL"
			value: "info"
		},
	]
	resources: {
		requests: {
			cpu:    "100m"
			memory: "128Mi"
		}
		limits: {
			cpu:    "500m"
			memory: "256Mi"
		}
	}
}

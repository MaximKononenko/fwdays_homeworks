# Timoni Web Application Module - Implementation

This directory contains a complete implementation of the Timoni homework assignment.

## Structure

```
timoni/
├── my-web-app/              # Main Timoni module
│   ├── timoni.cue           # Module workflow definition
│   ├── values.cue           # Default values
│   ├── templates/           # Kubernetes resource templates
│   │   ├── config.cue       # Configuration schema
│   │   ├── deployment.cue   # Deployment template
│   │   ├── service.cue      # Service template
│   │   ├── configmap.cue    # ConfigMap template
│   │   └── serviceaccount.cue
│   └── README.md
├── values-prod.cue          # Production environment values
├── values-staging.cue       # Staging environment values
├── bundle.cue               # Bundle definition for multi-environment deployment
└── IMPLEMENTATION.md        # This file
```

## Features Implemented

### Module Components
- ✅ **Deployment**: Nginx web server with configurable replicas
- ✅ **Service**: ClusterIP service exposing port 80
- ✅ **ConfigMap**: HTML content and nginx configuration
- ✅ **ServiceAccount**: For pod identity
- ✅ **Environment Variables**: Configurable env vars support
- ✅ **Resource Limits**: CPU and memory limits/requests
- ✅ **Health Checks**: Liveness and readiness probes

### Configuration Options
- `message`: Custom message displayed on the web page
- `image.repository` & `image.tag`: Container image configuration
- `replicas`: Number of pod replicas
- `service.port`: Service port
- `env`: Array of environment variables
- `resources`: CPU and memory requests/limits

## Usage

### Preview a Single Instance

Build and preview the production configuration:
```bash
cd /home/mkononen/pet-projects/fwdays_homeworks/timoni
timoni build web-prod ./my-web-app --namespace production -f values-prod.cue
```

Build and preview the staging configuration:
```bash
timoni build web-staging ./my-web-app --namespace staging -f values-staging.cue
```

### Preview Bundle (All Environments)

Preview all instances defined in the bundle:
```bash
timoni bundle build -f bundle.cue
```

### Deploy Single Instance

Deploy to production:
```bash
timoni apply web-prod ./my-web-app --namespace production -f values-prod.cue
```

Deploy to staging:
```bash
timoni apply web-staging ./my-web-app --namespace staging -f values-staging.cue
```

### Deploy Bundle

Deploy all instances at once:
```bash
timoni bundle apply -f bundle.cue
```

### Validate

Validate by building (dry-run):
```bash
timoni build web-prod ./my-web-app --namespace production -f values-prod.cue
```

### Update Deployment

After making changes to values or templates:
```bash
timoni apply web-prod ./my-web-app --namespace production -f values-prod.cue
```

### Check Status

View deployed instance status:
```bash
timoni status web-prod --namespace production
```

### List All Instances

```bash
timoni list --all-namespaces
```

### Delete Instance

```bash
timoni delete web-prod --namespace production
```

## Environment Configurations

### Production (`values-prod.cue`)
- 3 replicas for high availability
- Resource limits: 500m CPU, 256Mi memory
- Resource requests: 100m CPU, 128Mi memory
- Environment: production
- Log level: info

### Staging (`values-staging.cue`)
- 1 replica for cost efficiency
- Resource requests: 50m CPU, 64Mi memory
- Environment: staging
- Log level: debug

## Bundle Configuration

The `bundle.cue` file defines multiple instances that can be deployed together:
- **web-prod**: Production instance in `production` namespace
- **web-staging**: Staging instance in `staging` namespace

Both instances use the same module but with different configurations.

## Accessing the Application

After deployment, the application will be available via the Kubernetes Service:

```bash
# Port-forward to access locally
kubectl port-forward -n production svc/web-prod 8080:80

# Then open in browser
open http://localhost:8080
```

## Module Updates

To update the module after making changes:

1. Modify templates or values
2. Preview with `timoni build`
3. Apply changes with `timoni apply`

Example workflow:
```bash
# 1. Make changes to templates
vim my-web-app/templates/deployment.cue

# 2. Preview changes (validates automatically)
timoni build web-prod ./my-web-app --namespace production -f values-prod.cue

# 3. Apply
timoni apply web-prod ./my-web-app --namespace production -f values-prod.cue
```

## Key Concepts Demonstrated

1. **CUE Templates**: Using CUE language for type-safe configuration
2. **Module Composition**: Organizing Kubernetes resources in a reusable module
3. **Values Override**: Different configurations for different environments
4. **Bundle Management**: Deploying multiple instances with one command
5. **Immutable ConfigMaps**: ConfigMaps with content-based naming
6. **Health Checks**: Proper liveness and readiness probes
7. **Resource Management**: CPU and memory limits/requests
8. **Security**: Security contexts and capability management

## Bonus Features Implemented

- ✅ Health checks (liveness and readiness probes)
- ✅ Resource limits (CPU and memory)
- ✅ Multiple environment configurations
- ✅ Environment variables support
- ✅ Security contexts
- ✅ Immutable ConfigMaps

## Testing Checklist

- [x] Module initialization
- [x] Template creation (Deployment, Service, ConfigMap)
- [x] Values files for multiple environments
- [x] Bundle definition
- [x] Build preview works
- [x] Bundle build works
- [ ] Deploy to cluster
- [ ] Verify pods running
- [ ] Access application
- [ ] Test updates
- [ ] Test rollback

## Next Steps

To complete the homework:
1. Deploy to a Kubernetes cluster
2. Verify all resources are created correctly
3. Access the application and take screenshots
4. Test updating the module
5. Document any challenges and solutions

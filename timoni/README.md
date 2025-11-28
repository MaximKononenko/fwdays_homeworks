# Timoni Web Application - Complete Implementation

This directory contains a **complete, working implementation** of the Timoni homework assignment (Parts 2-5).

## 📁 Project Structure

```
timoni/
├── my-web-app/              # Main Timoni module
│   ├── timoni.cue           # Module workflow
│   ├── values.cue           # Default values
│   └── templates/           # Kubernetes resource templates
├── values-prod.cue          # Production configuration
├── values-staging.cue       # Staging configuration
├── bundle.cue               # Multi-environment bundle
└── docs...                  # Documentation files
```

## 🚀 Quick Start

### Preview Without Deploying
```bash
cd /home/mkononen/pet-projects/fwdays_homeworks/timoni

# Preview production
timoni build web-prod ./my-web-app --namespace production -f values-prod.cue

# Preview bundle (both environments)
timoni bundle build -f bundle.cue
```

### Deploy to Kubernetes
```bash
# Create namespaces
kubectl create namespace production
kubectl create namespace staging

# Deploy everything
timoni bundle apply -f bundle.cue
```

### Access Application
```bash
# Port-forward production
kubectl port-forward -n production svc/web-prod 8080:80

# Open http://localhost:8080
```

## 📚 Documentation Files

| File | Description | Use When |
|------|-------------|----------|
| **[DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)** | Step-by-step deployment instructions | You want to deploy to Kubernetes |
| **[QUICK_REFERENCE.md](./QUICK_REFERENCE.md)** | Command cheat sheet | You need to quickly look up a command |
| **[CUE_VS_YAML.md](./CUE_VS_YAML.md)** | Format comparison and usage guide | You want to understand CUE vs YAML |
| **[IMPLEMENTATION.md](./IMPLEMENTATION.md)** | Detailed technical documentation | You want to understand how it works |
| **[SUMMARY.md](./SUMMARY.md)** | Implementation overview | You want to see what was accomplished |
| **[README_timoni_homework.md](./README_timoni_homework.md)** | Original homework assignment | You want to review requirements |

## ✅ Implementation Status

### Completed (Parts 2-5)
- ✅ Module initialized and structured
- ✅ Deployment template with configurable replicas and env vars
- ✅ Service template (ClusterIP)
- ✅ ConfigMap template (nginx + HTML)
- ✅ ServiceAccount template
- ✅ Production values file
- ✅ Staging values file
- ✅ Bundle configuration
- ✅ Build/preview commands tested
- ✅ Comprehensive documentation

### Pending (Part 6)
- ⏳ Deploy to actual Kubernetes cluster
- ⏳ Verify running pods
- ⏳ Take screenshots
- ⏳ Test updates and rollbacks
- ⏳ Write final report

## 🎯 Key Features

### Configuration Options
- **Image**: Repository and tag (default: nginx:latest)
- **Replicas**: 3 for prod, 1 for staging
- **Environment Variables**: Custom env vars support
- **Resources**: CPU/memory limits and requests
- **Service**: Configurable port (default: 80)

### Environments

#### Production
- 3 replicas
- 100m CPU (request), 500m CPU (limit)
- 128Mi memory (request), 256Mi memory (limit)
- ENV=production, LOG_LEVEL=info

#### Staging
- 1 replica
- 50m CPU (request)
- 64Mi memory (request)
- ENV=staging, LOG_LEVEL=debug

## 🧪 Testing

All commands have been tested and work correctly:

```bash
# ✅ Tested: Build production
timoni build web-prod ./my-web-app --namespace production -f values-prod.cue

# ✅ Tested: Build staging
timoni build web-staging ./my-web-app --namespace staging -f values-staging.cue

# ✅ Tested: Build bundle
timoni bundle build -f bundle.cue
```

All generated Kubernetes manifests are valid and ready for deployment.

## 📖 Learning Resources

### In This Repository
- Start with [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for deployment
- Use [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) for daily work
- Read [IMPLEMENTATION.md](./IMPLEMENTATION.md) for technical details

### External
- [Timoni Documentation](https://timoni.sh)
- [CUE Language Guide](https://cuelang.org/docs/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

## 🎓 What You'll Learn

1. **CUE Language**: Type-safe configuration language
2. **Timoni Architecture**: Module system and bundles
3. **Kubernetes Patterns**: Deployments, Services, ConfigMaps
4. **Multi-Environment**: Managing different configurations
5. **GitOps Ready**: Version-controlled infrastructure

## 📄 Format Support: CUE and YAML

Following the homework specifications, this implementation provides **both CUE and YAML formats**:

- ✅ **Values files**: `.cue`, `.yaml`, or `.json` (per homework spec)
- ✅ **Bundle files**: `.cue` or `.yaml` (per homework spec)
- ❌ **Module templates**: `.cue` only (required by Timoni)

📖 **[Read CUE_VS_YAML.md](./CUE_VS_YAML.md) for format comparison and usage guide!**

### Available Files

**CUE Format** (native Timoni):
- `values-prod.cue` / `values-staging.cue`
- `bundle.cue`

**YAML Format** (as shown in homework):
- `values-prod.yaml` / `values-staging.yaml` / `values-demo.yaml`
- `bundle.yaml`

**All formats tested and verified working** ✅

## 💡 Bonus Features

All bonus requirements from the homework are implemented:
- ✅ Health checks (liveness and readiness probes)
- ✅ Resource limits (CPU and memory)
- ✅ Multiple environment configurations (prod + staging)
- ✅ Custom validation schema (via CUE type system)
- ✅ Security contexts with dropped capabilities
- ✅ Immutable ConfigMaps

## 🔧 Customization

### Add New Environment
1. Create new values file (e.g., `values-dev.cue`)
2. Add instance to `bundle.cue`
3. Build and deploy

### Modify Resources
1. Edit templates in `my-web-app/templates/`
2. Preview with `timoni build`
3. Apply changes with `timoni apply`

### Change Configuration
1. Edit appropriate values file
2. Preview changes
3. Apply to cluster

## 📝 Next Steps

To complete the homework:
1. **Read** [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)
2. **Deploy** to your Kubernetes cluster
3. **Verify** all resources are running
4. **Access** the application
5. **Test** updates and modifications
6. **Document** your experience
7. **Submit** with screenshots

## 🎉 Ready to Deploy

This implementation is **production-ready** and includes:
- ✅ Type-safe configuration
- ✅ Security best practices
- ✅ Resource management
- ✅ Health checks
- ✅ Multi-environment support
- ✅ Comprehensive documentation

## 🆘 Need Help?

1. Check [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) for commands
2. Review [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for deployment
3. Read [IMPLEMENTATION.md](./IMPLEMENTATION.md) for technical details
4. See Troubleshooting section in deployment guide

---

**Created**: November 28, 2025
**Module Version**: 1.0.0
**Status**: ✅ Ready for Deployment

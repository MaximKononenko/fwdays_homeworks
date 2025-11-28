# Deployment Guide - Timoni Web App

## Prerequisites
- Timoni CLI installed (✅ already installed)
- Kubernetes cluster access
- kubectl configured

## Quick Deploy

### Option 1: Deploy Both Environments (Recommended)
```bash
cd /home/mkononen/pet-projects/fwdays_homeworks/timoni

# Create namespaces
kubectl create namespace production
kubectl create namespace staging

# Deploy bundle
timoni bundle apply -f bundle.cue
```

### Option 2: Deploy Individual Environments

#### Production Only
```bash
kubectl create namespace production
timoni apply web-prod ./my-web-app --namespace production -f values-prod.cue
```

#### Staging Only
```bash
kubectl create namespace staging
timoni apply web-staging ./my-web-app --namespace staging -f values-staging.cue
```

## Verify Deployment

### Check Resources
```bash
# Production
kubectl get all -n production

# Staging
kubectl get all -n staging
```

### Check Pod Status
```bash
# Production (should have 3 pods)
kubectl get pods -n production

# Staging (should have 1 pod)
kubectl get pods -n staging
```

### View Logs
```bash
# Production
kubectl logs -n production -l app.kubernetes.io/name=web-prod

# Staging
kubectl logs -n staging -l app.kubernetes.io/name=web-staging
```

## Access Application

### Port Forward Method
```bash
# Production
kubectl port-forward -n production svc/web-prod 8080:80

# In another terminal - Staging
kubectl port-forward -n staging svc/web-staging 8081:80
```

Then open in browser:
- Production: http://localhost:8080
- Staging: http://localhost:8081

### Expected Output
You should see a web page with:
- Title: web-prod or web-staging
- Message: "Hello from Production Bundle from web-prod!" (or similar)
- Confirmation text about successful Timoni deployment

## Update Deployment

### Modify Values
Edit `values-prod.cue` or `values-staging.cue`, then:
```bash
timoni apply web-prod ./my-web-app --namespace production -f values-prod.cue
```

### Modify Templates
Edit files in `my-web-app/templates/`, then:
```bash
timoni apply web-prod ./my-web-app --namespace production -f values-prod.cue
```

## Check Status

### Using Timoni
```bash
timoni status web-prod --namespace production
timoni status web-staging --namespace staging
```

### Using kubectl
```bash
kubectl get deployment,service,configmap -n production
kubectl describe deployment web-prod -n production
```

## Troubleshooting

### Pods Not Starting
```bash
# Check pod status
kubectl get pods -n production

# Check pod details
kubectl describe pod <pod-name> -n production

# Check logs
kubectl logs <pod-name> -n production
```

### Image Pull Issues
Check if the nginx image is accessible:
```bash
kubectl describe pod <pod-name> -n production | grep -A 5 Events
```

### Service Not Accessible
```bash
# Check service
kubectl get svc -n production

# Check endpoints
kubectl get endpoints -n production
```

## Cleanup

### Delete Individual Instance
```bash
timoni delete web-prod --namespace production
timoni delete web-staging --namespace staging
```

### Delete Everything (Bundle)
```bash
timoni bundle delete -f bundle.cue

# Also delete namespaces
kubectl delete namespace production
kubectl delete namespace staging
```

## Testing Checklist

- [ ] Namespaces created
- [ ] Bundle or instances deployed successfully
- [ ] All pods running (3 in production, 1 in staging)
- [ ] Services created and endpoints populated
- [ ] ConfigMaps created with correct content
- [ ] Port-forward works
- [ ] Application accessible in browser
- [ ] Correct message displayed
- [ ] Environment variables set correctly
- [ ] Resource limits applied
- [ ] Health checks working

## Next Steps

After successful deployment:
1. Take screenshots of:
   - Running pods (`kubectl get pods`)
   - Application in browser
   - Timoni status output
2. Test updates by modifying values
3. Test rollback capabilities
4. Document any issues encountered
5. Complete homework submission

## Common Commands Reference

```bash
# List all Timoni instances
timoni list --all-namespaces

# Get detailed status
timoni status <instance-name> -n <namespace>

# Preview changes before applying
timoni build <instance-name> ./my-web-app -n <namespace> -f <values-file>

# Apply changes
timoni apply <instance-name> ./my-web-app -n <namespace> -f <values-file>

# Delete instance
timoni delete <instance-name> -n <namespace>
```

## Success Criteria

✅ All pods in Running state
✅ Services have endpoints
✅ Application accessible via port-forward
✅ Correct environment variables set
✅ Resource limits applied
✅ Health checks passing

# Timoni Quick Reference

## Most Used Commands

### Preview (Build without deploying)
```bash
# Single instance
timoni build <instance-name> <module-path> --namespace <namespace> -f <values-file>

# Bundle (all instances)
timoni bundle build -f <bundle-file>
```

### Deploy
```bash
# Single instance
timoni apply <instance-name> <module-path> --namespace <namespace> -f <values-file>

# Bundle (all instances)
timoni bundle apply -f <bundle-file>
```

### Validate (via build)
```bash
timoni build <instance-name> <module-path> --namespace <namespace> -f <values-file>
```

### Status & Management
```bash
# Check status
timoni status <instance-name> --namespace <namespace>

# List all instances
timoni list --all-namespaces

# Delete instance
timoni delete <instance-name> --namespace <namespace>
```

## Examples for This Module

### Production
```bash
# Preview
timoni build web-prod ./my-web-app --namespace production -f values-prod.cue

# Deploy
timoni apply web-prod ./my-web-app --namespace production -f values-prod.cue

# Status
timoni status web-prod --namespace production

# Delete
timoni delete web-prod --namespace production
```

### Staging
```bash
# Preview
timoni build web-staging ./my-web-app --namespace staging -f values-staging.cue

# Deploy
timoni apply web-staging ./my-web-app --namespace staging -f values-staging.cue
```

### Bundle (Both environments)
```bash
# Preview
timoni bundle build -f bundle.cue

# Deploy
timoni bundle apply -f bundle.cue

# Delete
timoni bundle delete -f bundle.cue
```

## Module Development Workflow

1. **Initialize**: `timoni mod init <module-name>`
2. **Edit templates**: Modify files in `templates/` directory
3. **Update values**: Edit `values.cue` and environment-specific files
4. **Preview**: `timoni build ...` to see generated YAML (also validates)
5. **Deploy**: `timoni apply ...` to deploy to cluster
6. **Update**: Repeat steps 2-5 as needed

## File Structure

```
my-web-app/
├── timoni.cue              # Module workflow and schema integration
├── values.cue              # Default values
├── templates/
│   ├── config.cue          # Configuration schema (#Config and #Instance)
│   ├── deployment.cue      # Deployment resource
│   ├── service.cue         # Service resource
│   ├── configmap.cue       # ConfigMap resource
│   └── serviceaccount.cue  # ServiceAccount resource
```

## Key CUE Concepts

- `#Config`: Schema definition for user values
- `#Instance`: Takes config and outputs Kubernetes objects
- `!:` Required field (must be provided by user)
- `*value`: Default value
- `_|_`: Bottom value (undefined/error)
- `if condition != _|_`: Conditional inclusion

## Common Issues

### Module not found
Ensure you're in the correct directory and use `./module-name` for local modules.

### Values validation error
Check that all required fields (marked with `!`) are provided in your values file.

### Bundle build fails
Ensure values are structs, not arrays. Use `values: { ... }` not `values: [{ ... }]`.

## Resources

- Timoni Documentation: https://timoni.sh
- CUE Language: https://cuelang.org
- Kubernetes API Reference: https://kubernetes.io/docs/reference/kubernetes-api/

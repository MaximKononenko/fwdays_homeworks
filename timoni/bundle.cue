bundle: {
	apiVersion: "v1alpha1"
	name:       "web-bundle"
	instances: {
		"web-prod": {
			module: {
				url:     "file://./my-web-app"
				version: "1.0.0"
			}
			namespace: "production"
			values: {
				message: "Hello from Production Bundle"
				image: {
					repository: "nginx"
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
		}
		"web-staging": {
			module: {
				url:     "file://./my-web-app"
				version: "1.0.0"
			}
			namespace: "staging"
			values: {
				message: "Hello from Staging Bundle"
				image: {
					repository: "nginx"
					tag:        "latest"
				}
				replicas: 1
				service: {
					port: 80
				}
				env: [
					{
						name:  "ENV"
						value: "staging"
					},
					{
						name:  "LOG_LEVEL"
						value: "debug"
					},
				]
				resources: {
					requests: {
						cpu:    "50m"
						memory: "64Mi"
					}
				}
			}
		}
	}
}

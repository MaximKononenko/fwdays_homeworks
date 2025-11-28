// Staging values for my-web-app

@if(!debug)

package main

values: {
	message: "Hello from Staging"
	image: {
		repository: "nginx"
		digest:     ""
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

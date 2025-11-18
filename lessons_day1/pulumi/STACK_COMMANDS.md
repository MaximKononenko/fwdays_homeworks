Helpful Pulumi stack commands

This short guide explains the most common stack commands you'll use when working with multiple Pulumi stacks (for example `dev` and `prod`). Use these when you want to list stacks, switch the active stack, inspect outputs, or destroy resources.

1) List stacks

```bash
pulumi stack ls
```
- Shows all stacks for the current Pulumi project. The currently selected stack is marked with an asterisk (*).

2) Select a stack

```bash
pulumi stack select dev
pulumi stack select prod
```
- Makes the named stack the active stack for subsequent Pulumi commands in the current working directory.
- After selecting, `pulumi up`, `pulumi preview`, `pulumi destroy`, `pulumi config`, and `pulumi stack output` operate against that stack.

3) Get stack outputs

```bash
pulumi stack output
```
- Prints the outputs exported by the currently selected stack (useful to retrieve endpoints or ports your program exported).

4) Destroy resources in a stack

```bash
pulumi stack select dev
pulumi destroy --yes
```
- `pulumi destroy` removes all resources managed by the selected stack.
- Use `--yes` to skip the interactive confirmation (handy for CI or scripts). Be careful: this is irreversible for the resources it destroys.

5) Remove a stack record

```bash
pulumi stack rm dev --yes
```
- Removes the stack record from the Pulumi backend after you have destroyed resources. Use `--yes` to skip confirmation.

6) Non-interactive / CI-friendly usage

- You can pass `--stack <org/project/stack>` to many Pulumi commands to avoid having to call `pulumi stack select` first. Example:

```bash
pulumi up --stack dev --yes
pulumi destroy --stack org/project/dev --yes
```

7) Safety tips

- Always run `pulumi stack ls` or `pulumi stack select` to check which stack is active before running destructive commands.
- For automation prefer explicit `--stack` usage and `--yes` to avoid interactive prompts.
- Keep local/backed-up Pulumi state if you might need to recover configuration or secrets before destroying stacks.

If you want, I can add a short link or a copy of this section into the main `README.md` for the assignment so students see it in context. Let me know and I'll patch the README for you.
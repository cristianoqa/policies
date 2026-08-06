# Flow Home Apps

## Sitio (cuando Pages funciona)
https://cristianoqa.github.io/policies/

## Vista previa inmediata (si Pages está en cola)
https://cdn.jsdelivr.net/gh/cristianoqa/policies@main/index.html

## Si Deploy site to Pages se queda en Queued
1. Cancela el run amarillo.
2. Actions → **Mirror site to gh-pages branch** → Run workflow.
3. Settings → Pages → Source = **Deploy from a branch** → `gh-pages` / root.

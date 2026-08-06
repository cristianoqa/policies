# Cómo dejar fija la web (léeme)

## Lo correcto en Settings → Pages

1. Entra: https://github.com/cristianoqa/policies/settings/pages  
2. **Source** = **Deploy from a branch** (NO GitHub Actions)  
3. **Branch** = **`gh-pages`**  
4. Folder = **`/ (root)`**  
5. **Save**

Si al recargar vuelve a “GitHub Actions”, vuelve a poner **branch → gh-pages** y Save otra vez.

## Cancela colas amarillas

Actions → cualquier run en **Queued** → **Cancel workflow**.

No hace falta “Mirror” ahora: ya empujé `main` → `gh-pages` con los últimos arreglos.

## Ver cambios ya (sin esperar a github.io)

https://cdn.jsdelivr.net/gh/cristianoqa/policies@9e17c30/index.html  

Luego Ctrl+F5 en: https://cristianoqa.github.io/policies/

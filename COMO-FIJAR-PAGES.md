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

El workflow `deploy-pages.yml` está **desactivado** (`.disabled`) para que no pelee con la rama `gh-pages`.

## Ver cambios YA (sin esperar a github.io)

https://cdn.jsdelivr.net/gh/cristianoqa/policies@main/index.html

Luego Ctrl+F5 en: https://cristianoqa.github.io/policies/

## Logo

- Marca página: `assets/flow-home-mark.png` (casa + ola)
- Card MyPass: `assets/mypass-app-icon.png` (mismo símbolo sobre squircle azul)
- El SVG viejo “MR” (`mypass-mark.svg`) se sobrescribió para que no vuelva a salir

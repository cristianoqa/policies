# Por qué github.io no cambia (y cómo verlo YA)

## Diagnóstico
Los builds de GitHub Pages de este repo están **atascados / cancelados / en error**.
Por eso `https://cristianoqa.github.io/policies/` se quedó congelado en una versión vieja
(logo MyPass “MR”).

No es un problema de tu ajuste “Deploy from a branch → gh-pages”: ese setting está bien.
El motor de build no termina de publicar la versión nueva.

## Ver la web correcta AHORA
Abre esto (Ctrl+clic):

https://cdn.jsdelivr.net/gh/cristianoqa/policies@main/docs/index.html

Ahí verás:
- Logo Flow Home Apps (casa + ola) en la cabecera
- MyPass con el mismo símbolo (no “MR”)
- Misma página lista para compartir

## Qué hacer en GitHub (5 minutos)
1. Actions → cancela TODO lo que esté Queued / Waiting / In progress  
2. Settings → Environments → **github-pages** → quita reglas de protección / branch policy  
3. Settings → Pages → Source = **Deploy from a branch** → `gh-pages` / root → Save  
4. Espera a que un build diga **built** (no errored)

Si Pages sigue muerto, la opción limpia es crear un repo nuevo solo para la landing
(por ejemplo `flow-home-apps`) y activar Pages ahí.

## Contenido ya listo en el repo
- `docs/` = sitio publicado (logo Flow Home)
- App MyPass local: logo actualizado en `D:\Mypass\assets\images\logomypass.png`

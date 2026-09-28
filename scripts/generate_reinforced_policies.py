#!/usr/bin/env python3
"""Generate reinforced GDPR-oriented privacy policies for Flow Home Apps."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIRS = [ROOT, ROOT / "docs"]
TODAY = "28 sep 2026"
TODAY_EN = "28 Sep 2026"
TODAY_PT = "28 set 2026"
CONTACT = "soporte.flowhomeapps@gmail.com"
AEPD = "https://www.aepd.es"

CSS_COMMON = """
    * {{ box-sizing: border-box; }}
    body {{
      margin:0;
      font-family:"Segoe UI",system-ui,sans-serif;
      background:
        radial-gradient(1200px 500px at 10% -10%, {glow1} 0%, transparent 55%),
        radial-gradient(900px 400px at 100% 0%, {glow2} 0%, transparent 50%),
        var(--bg);
      color:var(--ink);
      line-height:1.55;
    }}
    main {{ max-width:720px; margin:0 auto; padding:2.5rem 1.25rem 4rem; }}
    h1 {{ font-size:clamp(1.6rem,4vw,2.1rem); margin:0 0 .35rem; letter-spacing:-0.02em; }}
    .meta {{ color:var(--muted); font-size:.95rem; }}
    nav.langs {{ display:flex; flex-wrap:wrap; gap:.5rem; margin:1rem 0 1.5rem; }}
    nav.langs a {{
      color:var(--accent); text-decoration:none; border:1px solid var(--line);
      background:var(--card); border-radius:999px; padding:.35rem .85rem; font-size:.9rem;
    }}
    nav.langs a[aria-current="page"] {{ background:var(--ink); color:#fff; border-color:var(--ink); }}
    article {{
      background:var(--card); border:1px solid var(--line); border-radius:14px;
      padding:1.35rem 1.25rem 1.5rem;
    }}
    h2 {{ font-size:1.15rem; margin:1.4rem 0 .45rem; }}
    h2:first-child {{ margin-top:0; }}
    p, li {{ color:var(--ink); }}
    p {{ margin:.45rem 0; }}
    ul {{ padding-left:1.2rem; }}
    table {{ width:100%; border-collapse:collapse; margin:1rem 0; font-size:.95rem; }}
    th, td {{ border:1px solid var(--line); padding:8px 10px; text-align:left; vertical-align:top; }}
    th {{ background:rgba(0,0,0,.04); }}
    hr {{ border:0; border-top:1px solid var(--line); margin:1.25rem 0; }}
    footer {{ margin-top:1.5rem; color:var(--muted); font-size:.9rem; }}
    a {{ color:var(--accent); }}
    .note {{ font-size:.92rem; color:var(--muted); }}
"""

THEMES = {
    "lunera": dict(bg="#FBF9F6", ink="#2A2238", muted="#8B8399", card="#fff", accent="#4A3F6B", line="#E5DFEC", glow1="#F0E8F8", glow2="#FCEEF2"),
    "mypass": dict(bg="#f4f7fb", ink="#0d2847", muted="#4a5d73", card="#fff", accent="#1a6b9a", line="#d5e0ec", glow1="#d9ebf7", glow2="#e8f0e6"),
    "reformapro": dict(bg="#f3f8f8", ink="#102427", muted="#355457", card="#fff", accent="#0d7377", line="#cde4e5", glow1="#d7f1f2", glow2="#eef6f6"),
    "misiva": dict(bg="#f4f7fb", ink="#0d2847", muted="#4a5d73", card="#fff", accent="#1a6b9a", line="#d5e0ec", glow1="#d9ebf7", glow2="#e8f0e6"),
    "monexa": dict(bg="#f7f4f4", ink="#1a0f10", muted="#5a4548", card="#fff", accent="#c41e3a", line="#e5d6d8", glow1="#f3d4d8", glow2="#ece7e8"),
    "memio": dict(bg="#fff8f5", ink="#1a120e", muted="#5a4548", card="#fff", accent="#ff6b35", line="#ffd6c2", glow1="#ffe0d1", glow2="#fff1e8"),
    "miravista": dict(bg="#f4f7fb", ink="#0d2847", muted="#4a5d73", card="#fff", accent="#1a6b9a", line="#d5e0ec", glow1="#d9ebf7", glow2="#e8f0e6"),
}


def shell(theme: str, title: str, lang: str, meta: str, langs_nav: str, body: str, footer: str, extra_nav: str = "") -> str:
    t = THEMES[theme]
    css = CSS_COMMON.format(glow1=t["glow1"], glow2=t["glow2"])
    root = f":root {{ --bg:{t['bg']}; --ink:{t['ink']}; --muted:{t['muted']}; --card:{t['card']}; --accent:{t['accent']}; --line:{t['line']}; }}"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{title} (Flow Home Apps)." />
  <style>
    {root}
{css}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>{title}</h1>
      <p class="meta">{meta}</p>
      <nav class="langs" aria-label="Language">{langs_nav}</nav>
      {extra_nav}
    </header>
    <article>
{body}
    </article>
    <footer>{footer}</footer>
  </main>
</body>
</html>
"""


def nav(files: dict[str, str], current: str) -> str:
    labels = {"en": "English", "es": "Español", "pt": "Português"}
    parts = []
    for code, href in files.items():
        cur = ' aria-current="page"' if code == current else ""
        parts.append(f'<a href="./{href}"{cur}>{labels[code]}</a>')
    return "\n        ".join(parts)


# --- Shared GDPR blocks ---

def gdpr_es(*, bases: str, retention: str, recipients: str, transfers: str, minors: str = "13") -> str:
    return f"""
      <h2>Responsable del tratamiento</h2>
      <p><strong>Flow Home Apps</strong> (proyecto de desarrollo de aplicaciones independientes). Contacto de privacidad: <a href="mailto:{CONTACT}">{CONTACT}</a>. Si necesitas el NIF u otros datos identificativos del responsable para ejercer derechos, solicítalos por ese correo.</p>

      <h2>Base jurídica (RGPD)</h2>
      <ul>
{bases}
      </ul>

      <h2>Conservación</h2>
      <p>{retention}</p>

      <h2>Destinatarios y encargados</h2>
      <p>{recipients}</p>
      <p>No vendemos datos personales ni los cedemos para publicidad de terceros.</p>

      <h2>Transferencias internacionales</h2>
      <p>{transfers}</p>

      <h2>Tus derechos</h2>
      <p>Puedes ejercer acceso, rectificación, borrado, oposición, limitación y, cuando aplique, portabilidad, escribiendo a <a href="mailto:{CONTACT}">{CONTACT}</a>. Responderemos en el plazo legal.</p>
      <p>También puedes presentar una reclamación ante la <a href="{AEPD}" rel="noopener noreferrer" target="_blank">Agencia Española de Protección de Datos (AEPD)</a>.</p>

      <h2>Menores</h2>
      <p>La app no está dirigida a menores de {minors} años. Si detectamos datos de un menor sin base adecuada, los eliminaremos.</p>

      <h2>Seguridad</h2>
      <p>Aplicamos medidas técnicas razonables (cifrado en tránsito cuando hay red, almacenamiento local protegido por el sistema, y cifrado de extremo a extremo cuando la función lo indica). Ningún sistema es 100&nbsp;% seguro.</p>

      <h2>Cambios</h2>
      <p>Podemos actualizar esta política. La fecha de «Última actualización» refleja el cambio. Si el cambio es relevante, lo reflejaremos también en la ficha de la tienda cuando aplique.</p>

      <h2>Aviso</h2>
      <p class="note">Este documento describe el tratamiento real de la app y ayuda a cumplir el RGPD/LOPDGDD. No sustituye asesoramiento jurídico personalizado.</p>
"""


def gdpr_en(*, bases: str, retention: str, recipients: str, transfers: str, minors: str = "13") -> str:
    return f"""
      <h2>Data controller</h2>
      <p><strong>Flow Home Apps</strong> (independent app project). Privacy contact: <a href="mailto:{CONTACT}">{CONTACT}</a>. Tax ID or further controller details can be requested by email when exercising your rights.</p>

      <h2>Legal bases (GDPR)</h2>
      <ul>
{bases}
      </ul>

      <h2>Retention</h2>
      <p>{retention}</p>

      <h2>Recipients and processors</h2>
      <p>{recipients}</p>
      <p>We do not sell personal data or share it for third-party advertising.</p>

      <h2>International transfers</h2>
      <p>{transfers}</p>

      <h2>Your rights</h2>
      <p>You may request access, rectification, erasure, objection, restriction and, where applicable, portability at <a href="mailto:{CONTACT}">{CONTACT}</a>. We respond within legal deadlines.</p>
      <p>You may also lodge a complaint with your local supervisory authority (in Spain: <a href="{AEPD}" rel="noopener noreferrer" target="_blank">AEPD</a>).</p>

      <h2>Children</h2>
      <p>The app is not directed at children under {minors}. If we learn we hold such data without a valid basis, we will delete it.</p>

      <h2>Security</h2>
      <p>We apply reasonable measures (encryption in transit when online, OS-protected local storage, and end-to-end encryption where stated). No system is 100% secure.</p>

      <h2>Changes</h2>
      <p>We may update this policy. The “Last updated” date reflects changes. Material updates will also be reflected in the store listing when applicable.</p>

      <h2>Notice</h2>
      <p class="note">This document describes actual processing and supports GDPR compliance. It is not personalised legal advice.</p>
"""


def gdpr_pt(*, bases: str, retention: str, recipients: str, transfers: str, minors: str = "13") -> str:
    return f"""
      <h2>Responsável pelo tratamento</h2>
      <p><strong>Flow Home Apps</strong> (projeto independente de apps). Contacto de privacidade: <a href="mailto:{CONTACT}">{CONTACT}</a>. NIF ou outros dados do responsável podem ser pedidos por e-mail ao exercer direitos.</p>

      <h2>Base jurídica (RGPD)</h2>
      <ul>
{bases}
      </ul>

      <h2>Conservação</h2>
      <p>{retention}</p>

      <h2>Destinatários e subcontratantes</h2>
      <p>{recipients}</p>
      <p>Não vendemos dados pessoais nem os cedemos para publicidade de terceiros.</p>

      <h2>Transferências internacionais</h2>
      <p>{transfers}</p>

      <h2>Os seus direitos</h2>
      <p>Pode exercer acesso, retificação, apagamento, oposição, limitação e, quando aplicável, portabilidade em <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
      <p>Também pode apresentar reclamação à autoridade de controlo (em Espanha: <a href="{AEPD}" rel="noopener noreferrer" target="_blank">AEPD</a>; em Portugal: CNPD).</p>

      <h2>Menores</h2>
      <p>A app não se destina a menores de {minors} anos. Se detetarmos esses dados sem base adequada, eliminá-los-emos.</p>

      <h2>Segurança</h2>
      <p>Aplicamos medidas razoáveis (cifra em trânsito quando há rede, armazenamento local protegido pelo sistema e cifra ponta a ponta quando indicado). Nenhum sistema é 100&nbsp;% seguro.</p>

      <h2>Alterações</h2>
      <p>Podemos atualizar esta política. A data de atualização reflecte a mudança.</p>

      <h2>Aviso</h2>
      <p class="note">Este texto descreve o tratamento real e ajuda a cumprir o RGPD. Não substitui aconselhamento jurídico personalizado.</p>
"""


def write(name: str, html: str) -> None:
    for d in OUT_DIRS:
        d.mkdir(parents=True, exist_ok=True)
        (d / name).write_text(html, encoding="utf-8")
        print(f"wrote {d / name}")


# ========== APP CONTENT ==========

def lunera():
    files = {"en": "lunera.html", "es": "lunera-es.html", "pt": "lunera-pt.html"}
    # ES
    body_es = f"""
      <h2>Qué es Lunera</h2>
      <p>Lunera es una app <strong>FemTech de salud menstrual</strong> (Android y PWA). Predice fases del ciclo, registro de síntomas, calendario, etapas de vida, enciclopedia y asistencia IA local. Enfoque <strong>local-first</strong>.</p>
      <hr />
      <h2>Datos tratados</h2>
      <ul>
        <li>Registros diarios, ciclos, síntomas, configuración y preferencias (en el dispositivo).</li>
        <li>Modo invitado: sin cuenta en la nube.</li>
        <li>Biometría opcional: el sistema gestiona Face ID/huella; Lunera no guarda imágenes biométricas.</li>
        <li>PWA: datos mínimos en <code>localStorage</code> del navegador (este dispositivo).</li>
        <li>Si activas cuenta/sync: identificador de cuenta y backup <strong>cifrado</strong> (ciphertext) en el backend (p. ej. Supabase).</li>
      </ul>
      <h2>Datos de salud (categoría especial)</h2>
      <p>Los síntomas y el ciclo pueden constituir <strong>datos relativos a la salud</strong> (art. 9 RGPD). Solo se tratan con tu <strong>consentimiento explícito</strong> al usar esas funciones, o se quedan en el dispositivo bajo tu control. Lunera es educativa: no diagnostica ni receta.</p>
      <h2>Permisos</h2>
      <ul>
        <li>Notificaciones (recordatorios opcionales).</li>
        <li>Biometría (bloqueo opcional).</li>
        <li>Almacenamiento (backup / PDF).</li>
      </ul>
      <h2>Compras</h2>
      <p>Lunera Pro se gestiona en Google Play / App Store. Ko-fi/PayPal son apoyo voluntario y no desbloquean funciones digitales.</p>
""" + gdpr_es(
        bases="""        <li><strong>Ejecución del servicio / contrato</strong> (art. 6.1.b): prestarte la app que has instalado.</li>
        <li><strong>Consentimiento</strong> (art. 6.1.a y art. 9.2.a): datos de salud/síntomas y funciones opcionales (cuenta, sync, biometría, notificaciones).</li>
        <li><strong>Interés legítimo</strong> (art. 6.1.f): seguridad básica y respuesta a soporte, sin perjudicar tus derechos.</li>""",
        retention="En el dispositivo: mientras uses la app o hasta que borres datos/desinstales. Sync/backup en nube: mientras mantengas la cuenta o solicites borrado. Backups locales: bajo tu control.",
        recipients="Proveedores necesarios si activas sync (p. ej. Supabase) y tiendas (Google/Apple) para compras. La IA educativa local no envía tu historial a un servidor de Lunera.",
        transfers="Si usas sync, el proveedor cloud puede procesar datos fuera del EEE con garantías adecuadas (cláusulas tipo / medidas del proveedor). Sin sync, el tratamiento es local.",
        minors="16",
    )
    write(
        "lunera-es.html",
        shell(
            "lunera",
            "Política de privacidad — Lunera",
            "es",
            f"<strong>Responsable:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última actualización: {TODAY}",
            nav(files, "es"),
            body_es,
            "Flow Home Apps · Lunera",
            extra_nav=f'<p class="meta"><a href="./lunera-terms-es.html">Términos de servicio</a></p>',
        ),
    )

    body_en = f"""
      <h2>What Lunera is</h2>
      <p>Lunera is a <strong>FemTech menstrual-health</strong> app (Android + PWA). Cycle phases, symptom logging, calendar, life stages, encyclopedia and on-device educational AI. <strong>Local-first</strong>.</p>
      <hr />
      <h2>Data we process</h2>
      <ul>
        <li>Daily logs, cycles, symptoms, settings (on device).</li>
        <li>Guest mode: no cloud account.</li>
        <li>Optional biometrics: OS-managed; Lunera does not store biometric images.</li>
        <li>PWA: minimal data in browser <code>localStorage</code>.</li>
        <li>If you enable account/sync: account identifier and <strong>encrypted</strong> backup blob (e.g. Supabase).</li>
      </ul>
      <h2>Health data (special category)</h2>
      <p>Symptoms/cycle data may be <strong>health data</strong> (GDPR Art. 9). Processed with your <strong>explicit consent</strong> when you use those features, or kept on-device under your control. Lunera is educational—not a medical device.</p>
      <h2>Permissions</h2>
      <ul>
        <li>Notifications (optional reminders).</li>
        <li>Biometrics (optional lock).</li>
        <li>Storage (backup / PDF).</li>
      </ul>
      <h2>Purchases</h2>
      <p>Lunera Pro is handled by Google Play / App Store. Ko-fi/PayPal tips are voluntary and do not unlock Pro.</p>
""" + gdpr_en(
        bases="""        <li><strong>Contract / service</strong> (Art. 6(1)(b)): providing the app you installed.</li>
        <li><strong>Consent</strong> (Art. 6(1)(a) and 9(2)(a)): health/symptom data and optional features (account, sync, biometrics, notifications).</li>
        <li><strong>Legitimate interest</strong> (Art. 6(1)(f)): basic security and support replies.</li>""",
        retention="On device: while you use the app or until you delete/uninstall. Cloud sync: while the account exists or until deletion is requested.",
        recipients="Necessary processors if you enable sync (e.g. Supabase) and stores (Google/Apple) for purchases. Local educational AI does not upload your history to a Lunera server.",
        transfers="With sync, the cloud provider may process data outside the EEA under appropriate safeguards. Without sync, processing stays local.",
        minors="16",
    )
    write(
        "lunera.html",
        shell(
            "lunera",
            "Privacy policy — Lunera",
            "en",
            f"<strong>Controller:</strong> Flow Home Apps · <strong>Contact:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Last updated: {TODAY_EN}",
            nav(files, "en"),
            body_en,
            "Flow Home Apps · Lunera",
            extra_nav='<p class="meta"><a href="./lunera-terms.html">Terms of service</a></p>',
        ),
    )

    body_pt = f"""
      <h2>O que é a Lunera</h2>
      <p>Lunera é uma app <strong>FemTech de saúde menstrual</strong> (Android e PWA), com enfoque <strong>local-first</strong>.</p>
      <hr />
      <h2>Dados tratados</h2>
      <ul>
        <li>Registos, ciclos, sintomas e preferências no dispositivo.</li>
        <li>Modo convidado: sem conta na nuvem.</li>
        <li>Biometria opcional gerida pelo sistema.</li>
        <li>Com conta/sync: identificador e backup <strong>cifrado</strong> (p.ex. Supabase).</li>
      </ul>
      <h2>Dados de saúde</h2>
      <p>Podem ser <strong>dados de saúde</strong> (art. 9 RGPD). Tratados com <strong>consentimento explícito</strong> ou apenas no dispositivo. Lunera é educativa; não diagnostica.</p>
""" + gdpr_pt(
        bases="""        <li><strong>Execução do serviço</strong> (art. 6.º/1/b).</li>
        <li><strong>Consentimento</strong> (art. 6.º/1/a e 9.º/2/a) para dados de saúde e funções opcionais.</li>
        <li><strong>Interesse legítimo</strong> (art. 6.º/1/f) para segurança e suporte.</li>""",
        retention="No dispositivo até apagar/desinstalar. Na nuvem enquanto a conta existir ou pedir eliminação.",
        recipients="Fornecedores necessários se ativar sync (p.ex. Supabase) e lojas Google/Apple.",
        transfers="Com sync, o fornecedor cloud pode processar fora do EEE com salvaguardas adequadas.",
        minors="16",
    )
    write(
        "lunera-pt.html",
        shell(
            "lunera",
            "Política de privacidade — Lunera",
            "pt",
            f"<strong>Responsável:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última atualização: {TODAY_PT}",
            nav(files, "pt"),
            body_pt,
            "Flow Home Apps · Lunera",
            extra_nav='<p class="meta"><a href="./lunera-terms-pt.html">Termos de serviço</a></p>',
        ),
    )


def mypass():
    files = {"en": "mypass.html", "es": "mypass-es.html", "pt": "mypass-pt.html"}
    body_es = f"""
      <h2>Qué es MyPass</h2>
      <p>MyPass es una <strong>bóveda de contraseñas cifrada en tu dispositivo</strong>. La contraseña maestra no se envía en claro. No hay reset remoto por email/SMS; usa Recovery Key y backups cifrados. La copia en la nube (Supabase) es <strong>opcional</strong> y solo sube datos <strong>ya cifrados</strong>.</p>
      <hr />
      <h2>Datos en el dispositivo</h2>
      <ul>
        <li>Credenciales y contraseña maestra en memoria solo mientras usas la app.</li>
        <li>Bóveda cifrada y preferencias en almacenamiento seguro.</li>
        <li>Biometría: el sistema gestiona huella/rostro; MyPass no guarda imágenes biométricas.</li>
      </ul>
      <h2>Si activas la copia en la nube</h2>
      <ul>
        <li>Identidad de sesión (email u OAuth).</li>
        <li>Bóveda cifrada y metadatos de revisión. <strong>No</strong> se envía la contraseña maestra ni secretos en claro.</li>
      </ul>
      <h2>Permisos (Android)</h2>
      <ul>
        <li>Internet: solo con sync u OAuth.</li>
        <li>Biometría: desbloqueo opcional.</li>
      </ul>
""" + gdpr_es(
        bases="""        <li><strong>Ejecución del servicio</strong> (art. 6.1.b): bóveda local que has instalado.</li>
        <li><strong>Consentimiento</strong> (art. 6.1.a): sync cloud, OAuth y biometría opcionales.</li>
        <li><strong>Interés legítimo</strong> (art. 6.1.f): seguridad y soporte.</li>""",
        retention="Local: hasta que borres la bóveda o desinstales. Nube: mientras exista la cuenta o pidas borrado de objetos en Supabase.",
        recipients="Sin sync: nadie fuera del dispositivo. Con sync: Supabase (encargado/infraestructura) y, si usas OAuth, el proveedor de identidad (Google, etc.).",
        transfers="Con sync/OAuth, puede haber tratamiento fuera del EEE bajo las salvaguardas del proveedor. Sin sync, tratamiento local.",
    )
    write(
        "mypass-es.html",
        shell("mypass", "Política de privacidad — MyPass", "es",
              f"<strong>Responsable:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última actualización: {TODAY}",
              nav(files, "es"), body_es, "Flow Home Apps · MyPass"),
    )
    body_en = f"""
      <h2>What MyPass is</h2>
      <p>MyPass is an <strong>on-device encrypted password vault</strong>. The master password is never sent in clear text. Cloud backup (Supabase) is <strong>optional</strong> and uploads only <strong>already encrypted</strong> data.</p>
      <hr />
      <h2>On-device data</h2>
      <ul>
        <li>Credentials and master password in memory only while using the app.</li>
        <li>Encrypted vault and preferences in secure storage.</li>
        <li>Biometrics: OS-managed; MyPass does not store biometric images.</li>
      </ul>
      <h2>If you enable cloud backup</h2>
      <ul>
        <li>Session identity (email or OAuth).</li>
        <li>Encrypted vault + revision metadata. Master password and plaintext secrets are <strong>not</strong> uploaded.</li>
      </ul>
""" + gdpr_en(
        bases="""        <li><strong>Contract/service</strong> (Art. 6(1)(b)): local vault.</li>
        <li><strong>Consent</strong> (Art. 6(1)(a)): optional sync, OAuth, biometrics.</li>
        <li><strong>Legitimate interest</strong> (Art. 6(1)(f)): security and support.</li>""",
        retention="Local until vault wipe/uninstall. Cloud while the account exists or until deletion is requested.",
        recipients="No sync: device only. With sync: Supabase; with OAuth: identity provider.",
        transfers="Sync/OAuth may involve processing outside the EEA under provider safeguards.",
    )
    write(
        "mypass.html",
        shell("mypass", "Privacy policy — MyPass", "en",
              f"<strong>Controller:</strong> Flow Home Apps · <strong>Contact:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Last updated: {TODAY_EN}",
              nav(files, "en"), body_en, "Flow Home Apps · MyPass"),
    )
    body_pt = f"""
      <h2>O que é o MyPass</h2>
      <p>Cofre de palavras-passe <strong>cifrado no dispositivo</strong>. Backup na nuvem (Supabase) é <strong>opcional</strong> e só envia dados <strong>já cifrados</strong>.</p>
      <hr />
      <h2>Dados no dispositivo</h2>
      <ul>
        <li>Credenciais e palavra-passe mestra só em memória durante o uso.</li>
        <li>Cofre cifrado e preferências em armazenamento seguro.</li>
        <li>Biometria gerida pelo sistema.</li>
      </ul>
""" + gdpr_pt(
        bases="""        <li><strong>Execução do serviço</strong> (art. 6.º/1/b).</li>
        <li><strong>Consentimento</strong> para sync/OAuth/biometria.</li>
        <li><strong>Interesse legítimo</strong> para segurança e suporte.</li>""",
        retention="Local até apagar/desinstalar. Nuvem enquanto a conta existir.",
        recipients="Sem sync: só o dispositivo. Com sync: Supabase; com OAuth: fornecedor de identidade.",
        transfers="Sync/OAuth podem implicar tratamento fora do EEE com salvaguardas.",
    )
    write(
        "mypass-pt.html",
        shell("mypass", "Política de privacidade — MyPass", "pt",
              f"<strong>Responsável:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última atualização: {TODAY_PT}",
              nav(files, "pt"), body_pt, "Flow Home Apps · MyPass"),
    )


def reformapro():
    files = {"en": "reformapro.html", "es": "reformapro-es.html", "pt": "reformapro-pt.html"}
    body_es = f"""
      <h2>Qué es ReformaPRO</h2>
      <p>App para <strong>crear y gestionar presupuestos de reformas</strong>: clientes, catálogo, líneas, impuestos, márgenes, PDF y envío.</p>
      <hr />
      <h2>Roles</h2>
      <ul>
        <li><strong>Flow Home Apps</strong> es responsable del tratamiento de tu cuenta (email, autenticación) y de la infraestructura que almacena los datos de la app.</li>
        <li>Los datos de <strong>tus clientes</strong> (nombre, teléfono, email, dirección, presupuestos) los introduces tú: debes disponer de base legítima frente a ellos (relación comercial). Flow Home Apps los trata para prestarte el servicio.</li>
      </ul>
      <h2>Datos que tratamos</h2>
      <ul>
        <li>Cuenta: email y autenticación.</li>
        <li>Negocio: clientes, catálogo, presupuestos, plantillas y documentos generados.</li>
      </ul>
      <h2>Dónde se guardan</h2>
      <p>En infraestructura cloud operada para ReformaPRO (p. ej. base de datos/hosting del proyecto) y preferencias temporales en el dispositivo.</p>
      <h2>Permisos</h2>
      <ul><li>Internet: sesión, sincronización y documentos.</li></ul>
""" + gdpr_es(
        bases="""        <li><strong>Ejecución del contrato</strong> (art. 6.1.b): cuenta y servicio de presupuestos.</li>
        <li><strong>Interés legítimo</strong> (art. 6.1.f): seguridad, prevención de abuso y soporte.</li>
        <li>Respecto a los datos de tus clientes: tú garantizas que puedes facilitarlos; nosotros los tratamos para ejecutar el servicio contigo.</li>""",
        retention="Mientras mantengas la cuenta activa. Tras borrado de cuenta o solicitud, eliminamos o anonimizamos en un plazo razonable salvo obligación legal de conservación (p. ej. facturación si existiera).",
        recipients="Proveedores de hosting/base de datos necesarios para operar la app. No vendemos datos. Si envías un PDF por WhatsApp/email, el canal lo eliges tú.",
        transfers="La infraestructura cloud puede estar fuera del EEE; usamos proveedores con salvaguardas adecuadas cuando aplique.",
    )
    write(
        "reformapro-es.html",
        shell("reformapro", "Política de privacidad — ReformaPRO", "es",
              f"<strong>Responsable:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última actualización: {TODAY}",
              nav(files, "es"), body_es, "Flow Home Apps · ReformaPRO"),
    )
    body_en = f"""
      <h2>What ReformaPRO is</h2>
      <p>App to <strong>create and manage renovation quotes</strong>: clients, catalogue, lines, taxes, margins, PDF and sharing.</p>
      <hr />
      <h2>Roles</h2>
      <ul>
        <li><strong>Flow Home Apps</strong> is controller for your account and the app infrastructure.</li>
        <li><strong>Your clients’ data</strong> is entered by you; you must have a lawful basis toward them. We process it to provide the service to you.</li>
      </ul>
      <h2>Data we process</h2>
      <ul>
        <li>Account: email and authentication.</li>
        <li>Business: clients, catalogue, quotes, templates and generated documents.</li>
      </ul>
""" + gdpr_en(
        bases="""        <li><strong>Contract</strong> (Art. 6(1)(b)): account and quoting service.</li>
        <li><strong>Legitimate interest</strong> (Art. 6(1)(f)): security and support.</li>
        <li>For your clients’ data: you warrant you may provide it; we process it to perform the service.</li>""",
        retention="While the account is active; after deletion request we erase or anonymise within a reasonable time unless law requires retention.",
        recipients="Hosting/database providers needed to run the app. We do not sell data.",
        transfers="Cloud infrastructure may be outside the EEA under appropriate safeguards.",
    )
    write(
        "reformapro.html",
        shell("reformapro", "Privacy policy — ReformaPRO", "en",
              f"<strong>Controller:</strong> Flow Home Apps · <strong>Contact:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Last updated: {TODAY_EN}",
              nav(files, "en"), body_en, "Flow Home Apps · ReformaPRO"),
    )
    body_pt = f"""
      <h2>O que é o ReformaPRO</h2>
      <p>App para <strong>orçamentos de reformas</strong>: clientes, catálogo, impostos, PDF e envio.</p>
      <hr />
      <h2>Papéis</h2>
      <ul>
        <li><strong>Flow Home Apps</strong> é responsável pela sua conta e infraestrutura.</li>
        <li>Os dados dos <strong>seus clientes</strong> são introduzidos por si; deve ter base legítima perante eles.</li>
      </ul>
""" + gdpr_pt(
        bases="""        <li><strong>Execução do contrato</strong> (art. 6.º/1/b).</li>
        <li><strong>Interesse legítimo</strong> (art. 6.º/1/f) para segurança e suporte.</li>""",
        retention="Enquanto a conta estiver ativa; após pedido de eliminação, apagamos ou anonimizamos em prazo razoável.",
        recipients="Fornecedores de hosting/BD necessários. Não vendemos dados.",
        transfers="A cloud pode estar fora do EEE com salvaguardas adequadas.",
    )
    write(
        "reformapro-pt.html",
        shell("reformapro", "Política de privacidade — ReformaPRO", "pt",
              f"<strong>Responsável:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última atualização: {TODAY_PT}",
              nav(files, "pt"), body_pt, "Flow Home Apps · ReformaPRO"),
    )


def misiva():
    files = {"en": "misiva.html", "es": "mensajetexto.html", "pt": "misiva-pt.html"}
    body_es = f"""
      <h2>Resumen</h2>
      <p>Misiva (antes MensajeTexto) genera mensajes con Google Gemini y los envía por WhatsApp según programaciones que defines. Los datos de la app se almacenan <strong>en tu dispositivo</strong>. No operamos servidores propios que reciban el contenido de tus mensajes.</p>
      <hr />
      <h2>Datos que procesamos</h2>
      <table>
        <thead><tr><th>Dato</th><th>Uso</th><th>Dónde</th></tr></thead>
        <tbody>
          <tr><td>Teléfonos de destinatarios</td><td>Envío por WhatsApp</td><td>Base local</td></tr>
          <tr><td>Contactos (opcional)</td><td>Autocompletar</td><td>Solo lectura en el dispositivo</td></tr>
          <tr><td>Prompts / instrucciones</td><td>Generar texto con Gemini</td><td>Local + envío a Google si usas API Key</td></tr>
          <tr><td>API Key de Gemini</td><td>Llamadas a Google</td><td>Cifrada en el dispositivo</td></tr>
          <tr><td>Historial y cola de envíos</td><td>Funcionamiento de la app</td><td>Local (TTL en diferidos)</td></tr>
        </tbody>
      </table>
      <h2>Servicios de terceros</h2>
      <ul>
        <li><strong>Google Gemini API:</strong> los prompts se envían a Google. Ver <a href="https://policies.google.com/privacy">política de Google</a>.</li>
        <li><strong>WhatsApp (Meta):</strong> se abre en tu dispositivo; Misiva no habla con servidores de Meta por su cuenta.</li>
      </ul>
      <h2>AccessibilityService</h2>
      <p>Solo para automatizar el envío en WhatsApp (localizar/pulsar Enviar) en el momento programado o tras confirmación. No se usa para leer otras apps con fines ajenos ni para enviar contenido a servidores de Flow Home Apps.</p>
      <h2>Permisos</h2>
      <ul>
        <li>Internet (Gemini), notificaciones, alarmas exactas, inicio tras reinicio, primer plano, contactos (opcional).</li>
      </ul>
""" + gdpr_es(
        bases="""        <li><strong>Ejecución del servicio</strong> (art. 6.1.b): programar y enviar los mensajes que defines.</li>
        <li><strong>Consentimiento</strong> (art. 6.1.a): API Key, contactos, AccessibilityService y notificaciones.</li>
        <li><strong>Interés legítimo</strong> (art. 6.1.f): seguridad local y soporte.</li>""",
        retention="Hasta que borres historial/envíos/API Key en la app o desinstales. Envíos diferidos caducan solos (ventana limitada). allowBackup=false.",
        recipients="Google (Gemini) si usas API Key; WhatsApp/Meta solo a través de la app que abres tú. Flow Home Apps no recibe el contenido de tus mensajes en servidores propios.",
        transfers="Las llamadas a Gemini pueden implicar tratamiento por Google fuera del EEE según su política.",
    )
    write(
        "mensajetexto.html",
        shell("misiva", "Política de privacidad — Misiva", "es",
              f"<strong>Responsable:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última actualización: {TODAY}",
              nav(files, "es"), body_es, "Flow Home Apps · Misiva"),
    )
    body_en = f"""
      <h2>Summary</h2>
      <p>Misiva generates messages with Google Gemini and sends them via WhatsApp on schedules you define. App data stays <strong>on your device</strong>. We do not run our own servers that receive your message content.</p>
      <hr />
      <h2>Data processed</h2>
      <ul>
        <li>Recipient numbers, optional contacts, prompts, Gemini API key (encrypted on device), send history/queue.</li>
      </ul>
      <h2>Third parties</h2>
      <ul>
        <li><strong>Google Gemini:</strong> prompts go to Google if you set an API key.</li>
        <li><strong>WhatsApp (Meta):</strong> opened on your device.</li>
      </ul>
      <h2>AccessibilityService</h2>
      <p>Only to automate tapping Send in WhatsApp at schedule/confirmation time. Not used to scrape other apps or upload content to Flow Home Apps servers.</p>
""" + gdpr_en(
        bases="""        <li><strong>Contract/service</strong> (Art. 6(1)(b)).</li>
        <li><strong>Consent</strong> (Art. 6(1)(a)) for API key, contacts, AccessibilityService, notifications.</li>
        <li><strong>Legitimate interest</strong> (Art. 6(1)(f)) for local security and support.</li>""",
        retention="Until you clear data or uninstall. Deferred sends expire. allowBackup=false.",
        recipients="Google (Gemini) if API key used; WhatsApp via the app you open. We do not host your message content.",
        transfers="Gemini calls may involve Google processing outside the EEA.",
    )
    write(
        "misiva.html",
        shell("misiva", "Privacy policy — Misiva", "en",
              f"<strong>Controller:</strong> Flow Home Apps · <strong>Contact:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Last updated: {TODAY_EN}",
              nav(files, "en"), body_en, "Flow Home Apps · Misiva"),
    )
    body_pt = f"""
      <h2>Resumo</h2>
      <p>Misiva gera mensagens com Google Gemini e envia via WhatsApp. Os dados ficam <strong>no dispositivo</strong>.</p>
      <hr />
      <h2>Dados</h2>
      <ul>
        <li>Números, contactos opcionais, prompts, API Key Gemini (cifrada), histórico/fila.</li>
      </ul>
      <h2>AccessibilityService</h2>
      <p>Apenas para automatizar o Enviar no WhatsApp no momento agendado.</p>
""" + gdpr_pt(
        bases="""        <li><strong>Execução do serviço</strong> (art. 6.º/1/b).</li>
        <li><strong>Consentimento</strong> para API Key, contactos, acessibilidade e notificações.</li>
        <li><strong>Interesse legítimo</strong> para segurança e suporte.</li>""",
        retention="Até apagar dados ou desinstalar. Envios diferidos expiram.",
        recipients="Google (Gemini) se usar API Key; WhatsApp através da app que abre.",
        transfers="Chamadas Gemini podem implicar tratamento fora do EEE pela Google.",
    )
    write(
        "misiva-pt.html",
        shell("misiva", "Política de privacidade — Misiva", "pt",
              f"<strong>Responsável:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última atualização: {TODAY_PT}",
              nav(files, "pt"), body_pt, "Flow Home Apps · Misiva"),
    )


def monexa():
    files = {"en": "monexa.html", "es": "monexa-es.html", "pt": "monexa-pt.html"}
    body_es = f"""
      <h2>Qué es Monexa</h2>
      <p>App de <strong>control de gastos e ingresos compartidos</strong> (antes GastoControl): movimientos, categorías, presupuestos, suscripciones y metas en grupo.</p>
      <hr />
      <h2>Datos que tratamos</h2>
      <ul>
        <li>Cuenta: email y autenticación (Firebase Auth).</li>
        <li>Uso: gastos/ingresos, categorías, notas, presupuestos, suscripciones, metas y membresía del grupo (Firestore).</li>
        <li>Opcional: imágenes de tickets (OCR) y micrófono (voz).</li>
      </ul>
      <h2>Dónde se guardan</h2>
      <p>Cuenta y grupo en <strong>Google Firebase</strong> (proyecto Flow Home Apps). Preferencias locales en el dispositivo.</p>
      <h2>Permisos</h2>
      <ul>
        <li>Internet, cámara/fotos (tickets), micrófono (voz) — opcionales según función.</li>
      </ul>
""" + gdpr_es(
        bases="""        <li><strong>Ejecución del contrato</strong> (art. 6.1.b): cuenta y sincronización del grupo.</li>
        <li><strong>Consentimiento</strong> (art. 6.1.a): cámara, micrófono, OCR de terceros.</li>
        <li><strong>Interés legítimo</strong> (art. 6.1.f): seguridad y soporte.</li>""",
        retention="Mientras la cuenta/grupo existan. Puedes borrar movimientos o solicitar borrado de cuenta a soporte. Datos locales se eliminan al desinstalar.",
        recipients="Google Firebase/Google Cloud. Si usas OCR de terceros (p. ej. OCR.space), la imagen puede enviarse a ese servicio según su política. Miembros de tu grupo ven los datos del grupo.",
        transfers="Firebase/Google pueden procesar fuera del EEE bajo sus salvaguardas contractuales.",
    )
    write(
        "monexa-es.html",
        shell("monexa", "Política de privacidad — Monexa", "es",
              f"<strong>Responsable:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última actualización: {TODAY}",
              nav(files, "es"), body_es, "Flow Home Apps · Monexa",
              extra_nav='<p class="meta"><a href="./monexa-terms-es.html">Términos de servicio</a></p>'),
    )
    body_en = f"""
      <h2>What Monexa is</h2>
      <p><strong>Shared expense tracker</strong>: movements, categories, budgets, subscriptions and goals in a group.</p>
      <hr />
      <h2>Data</h2>
      <ul>
        <li>Account via Firebase Auth; group data in Firestore; optional ticket OCR and voice input.</li>
      </ul>
""" + gdpr_en(
        bases="""        <li><strong>Contract</strong> (Art. 6(1)(b)).</li>
        <li><strong>Consent</strong> (Art. 6(1)(a)) for camera, mic, third-party OCR.</li>
        <li><strong>Legitimate interest</strong> (Art. 6(1)(f)).</li>""",
        retention="While account/group exist; delete movements in-app or request account deletion.",
        recipients="Google Firebase; optional OCR providers; your group members see group data.",
        transfers="Firebase/Google may process outside the EEA under their safeguards.",
    )
    write(
        "monexa.html",
        shell("monexa", "Privacy policy — Monexa", "en",
              f"<strong>Controller:</strong> Flow Home Apps · <strong>Contact:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Last updated: {TODAY_EN}",
              nav(files, "en"), body_en, "Flow Home Apps · Monexa",
              extra_nav='<p class="meta"><a href="./monexa-terms.html">Terms of service</a></p>'),
    )
    body_pt = f"""
      <h2>O que é a Monexa</h2>
      <p>Controlo de <strong>despesas partilhadas</strong> com Firebase.</p>
      <hr />
      <h2>Dados</h2>
      <ul>
        <li>Conta (Firebase Auth), dados do grupo (Firestore), OCR/voz opcionais.</li>
      </ul>
""" + gdpr_pt(
        bases="""        <li><strong>Execução do contrato</strong>.</li>
        <li><strong>Consentimento</strong> para câmara, microfone e OCR.</li>
        <li><strong>Interesse legítimo</strong> para segurança e suporte.</li>""",
        retention="Enquanto a conta/grupo existirem; pode pedir eliminação.",
        recipients="Google Firebase; OCR de terceiros se ativar; membros do grupo.",
        transfers="Firebase/Google podem processar fora do EEE.",
    )
    write(
        "monexa-pt.html",
        shell("monexa", "Política de privacidade — Monexa", "pt",
              f"<strong>Responsável:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última atualização: {TODAY_PT}",
              nav(files, "pt"), body_pt, "Flow Home Apps · Monexa",
              extra_nav='<p class="meta"><a href="./monexa-terms-pt.html">Termos de serviço</a></p>'),
    )


def memio():
    files = {"en": "memio.html", "es": "memio-es.html", "pt": "memio-pt.html"}
    body_es = f"""
      <h2>Qué es Memio</h2>
      <p>Generador de memes para Android. Procesa imágenes <strong>en el dispositivo</strong>. No requiere cuenta.</p>
      <hr />
      <h2>Datos</h2>
      <ul>
        <li>Fotos elegidas y memes generados: procesamiento local.</li>
        <li>Lista de recientes en almacenamiento de la app.</li>
        <li>Si guardas/compartes, usas el selector del sistema.</li>
      </ul>
      <h2>Qué no hacemos</h2>
      <ul>
        <li>No sincronizamos tus imágenes con un servidor de Memio.</li>
        <li>No vendemos datos ni publicidad invasiva de terceros.</li>
      </ul>
""" + gdpr_es(
        bases="""        <li><strong>Ejecución del servicio</strong> (art. 6.1.b): generar memes localmente.</li>
        <li><strong>Consentimiento</strong> (art. 6.1.a): acceso a fotos/galería cuando lo concedes.</li>""",
        retention="Hasta que borres memes o desinstales la app. Imágenes en la galería quedan bajo tu control.",
        recipients="Ninguno por defecto. Si compartes un meme, el destino (WhatsApp, etc.) lo eliges tú.",
        transfers="Sin transferencias internacionales por parte de Memio en el uso normal.",
    )
    write(
        "memio-es.html",
        shell("memio", "Política de privacidad — Memio", "es",
              f"<strong>Responsable:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última actualización: {TODAY}",
              nav(files, "es"), body_es, "Flow Home Apps · Memio"),
    )
    body_en = f"""
      <h2>What Memio is</h2>
      <p>Android meme generator. Images are processed <strong>on device</strong>. No account required.</p>
      <hr />
      <h2>Data</h2>
      <ul>
        <li>Chosen photos and generated memes: local processing; recent list in app storage.</li>
      </ul>
""" + gdpr_en(
        bases="""        <li><strong>Contract/service</strong> (Art. 6(1)(b)).</li>
        <li><strong>Consent</strong> (Art. 6(1)(a)) for gallery access.</li>""",
        retention="Until you delete memes or uninstall. Gallery copies remain under your control.",
        recipients="None by default; share targets are chosen by you.",
        transfers="No international transfers by Memio in normal use.",
    )
    write(
        "memio.html",
        shell("memio", "Privacy policy — Memio", "en",
              f"<strong>Controller:</strong> Flow Home Apps · <strong>Contact:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Last updated: {TODAY_EN}",
              nav(files, "en"), body_en, "Flow Home Apps · Memio"),
    )
    body_pt = f"""
      <h2>O que é o Memio</h2>
      <p>Gerador de memes <strong>no dispositivo</strong>, sem conta.</p>
""" + gdpr_pt(
        bases="""        <li><strong>Execução do serviço</strong>.</li>
        <li><strong>Consentimento</strong> para acesso à galeria.</li>""",
        retention="Até apagar memes ou desinstalar.",
        recipients="Nenhum por defeito; partilha é escolha sua.",
        transfers="Sem transferências internacionais no uso normal.",
    )
    write(
        "memio-pt.html",
        shell("memio", "Política de privacidade — Memio", "pt",
              f"<strong>Responsável:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última atualização: {TODAY_PT}",
              nav(files, "pt"), body_pt, "Flow Home Apps · Memio"),
    )


def miravista():
    files = {"en": "miravista.html", "es": "miravista-es.html", "pt": "miravista-pt.html"}
    body_es = f"""
      <h2>Resumen</h2>
      <p>Miravista transmite la pantalla (y audio de reproducción si lo permites) <strong>solo en tu Wi‑Fi local</strong>. No opera servidores en la nube para el mirroring.</p>
      <hr />
      <h2>Datos</h2>
      <table>
        <tr><th>Dato</th><th>Finalidad</th><th>Dónde</th></tr>
        <tr><td>Contenido de pantalla</td><td>Stream MJPEG</td><td>Dispositivo + LAN</td></tr>
        <tr><td>Audio (opcional)</td><td>Stream PCM</td><td>Con MediaProjection</td></tr>
        <tr><td>IP local / PIN</td><td>URL y autenticación local</td><td>Dispositivo</td></tr>
      </table>
      <h2>Red local</h2>
      <p>Servidor HTTP en el puerto <strong>8080</strong>. Quien tenga la URL con PIN puede ver el stream. Detén el mirroring cuando no lo uses.</p>
""" + gdpr_es(
        bases="""        <li><strong>Ejecución del servicio</strong> (art. 6.1.b): espejo local que inicias tú.</li>
        <li><strong>Consentimiento</strong> (art. 6.1.a): captura de pantalla/audio (MediaProjection).</li>""",
        retention="El stream es en tiempo real; no almacenamos capturas en servidores de Miravista. Preferencias locales hasta desinstalar.",
        recipients="Solo dispositivos de tu LAN a los que des acceso (URL+PIN). No hay analytics de terceros en esta versión.",
        transfers="Sin transferencias internacionales: el tráfico no sale de tu red local en el uso previsto.",
    )
    write(
        "miravista-es.html",
        shell("miravista", "Política de privacidad — Miravista", "es",
              f"<strong>Responsable:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última actualización: {TODAY}",
              nav(files, "es"), body_es, "Flow Home Apps · Miravista"),
    )
    body_en = f"""
      <h2>Summary</h2>
      <p>Miravista mirrors your screen (and optional playback audio) <strong>on your local Wi‑Fi only</strong>. No cloud mirroring servers.</p>
      <hr />
      <h2>Data</h2>
      <ul>
        <li>Screen/audio stream on LAN; local IP and session PIN on device.</li>
      </ul>
""" + gdpr_en(
        bases="""        <li><strong>Contract/service</strong> (Art. 6(1)(b)).</li>
        <li><strong>Consent</strong> (Art. 6(1)(a)) for MediaProjection capture.</li>""",
        retention="Real-time stream only; no cloud storage of captures by Miravista.",
        recipients="Only LAN devices you share URL+PIN with.",
        transfers="No international transfers in intended use (stays on LAN).",
    )
    write(
        "miravista.html",
        shell("miravista", "Privacy policy — Miravista", "en",
              f"<strong>Controller:</strong> Flow Home Apps · <strong>Contact:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Last updated: {TODAY_EN}",
              nav(files, "en"), body_en, "Flow Home Apps · Miravista"),
    )
    body_pt = f"""
      <h2>Resumo</h2>
      <p>Miravista espelha o ecrã <strong>só na Wi‑Fi local</strong>, sem servidores cloud de mirroring.</p>
""" + gdpr_pt(
        bases="""        <li><strong>Execução do serviço</strong>.</li>
        <li><strong>Consentimento</strong> para captura (MediaProjection).</li>""",
        retention="Stream em tempo real; sem armazenamento cloud pela Miravista.",
        recipients="Apenas dispositivos da LAN com URL+PIN.",
        transfers="Sem transferências internacionais no uso previsto.",
    )
    write(
        "miravista-pt.html",
        shell("miravista", "Política de privacidade — Miravista", "pt",
              f"<strong>Responsável:</strong> Flow Home Apps · <strong>Contacto:</strong> <a href=\"mailto:{CONTACT}\">{CONTACT}</a><br />Última atualização: {TODAY_PT}",
              nav(files, "pt"), body_pt, "Flow Home Apps · Miravista"),
    )


def update_index_and_readme():
    readme = f"""# Políticas de privacidad (Flow Home Apps)

Sitio publicado: https://cristianoqa.github.io/policies/

Actualización reforzada RGPD: {TODAY} (bases jurídicas, conservación, destinatarios, transferencias, derechos + AEPD).

- MyPass: mypass-es.html / mypass.html / mypass-pt.html
- Misiva: mensajetexto.html / misiva.html / misiva-pt.html
- Miravista: miravista-es.html (EN/PT; screenmirror-* redirige)
- Monexa: monexa-es.html / monexa.html / monexa-pt.html (+ términos)
- Memio: memio-es.html / memio.html / memio-pt.html
- Lunera: lunera-es.html / lunera.html / lunera-pt.html (+ términos)
- ReformaPRO: reformapro-es.html / reformapro.html / reformapro-pt.html

Regenerar: `python scripts/generate_reinforced_policies.py`

Landing: https://cristianoqa.github.io/
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    (ROOT / "docs" / "README.md").write_text(readme, encoding="utf-8")
    print("wrote README.md")


def main():
    lunera()
    mypass()
    reformapro()
    misiva()
    monexa()
    memio()
    miravista()
    update_index_and_readme()
    print("OK")


if __name__ == "__main__":
    main()

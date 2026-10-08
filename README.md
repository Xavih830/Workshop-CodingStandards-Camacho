# Workshop Coding Standards (Java y Python)

Repositorio preparado para el workshop de Ingeniería de Software (ESPOL) enfocado en la aplicación de estándares de codificación mediante herramientas de análisis estático en Java y Python.

## Estructura del Proyecto

```
workshop-coding-standards/
  README.md
  .gitignore
  java/
    src/                     # Código fuente Java a evaluar
    tools/                   # Artefactos y binarios de analizadores (Checkstyle, PMD)
    run_checkstyle_sun.ps1   # Script de análisis Checkstyle (Sun Checks)
    run_checkstyle_google.ps1# Script de análisis Checkstyle (Google Checks)
    run_pmd.ps1              # Script de análisis PMD (Quickstart)
  python/
    src/                     # Código fuente Python a evaluar
    requirements.txt         # Dependencias (pylint, flake8)
    run_pylint.ps1           # Script de análisis Pylint
    run_flake8.ps1           # Script de análisis Flake8
  reports/
    initial/                 # Reportes generados en fase inicial
    final/                   # Reportes generados en fase final
    ensayo/                  # Reportes de prueba de humo
  evidencias/                # Capturas de pantalla y evidencias
  informe/
    plantilla_informe.md     # Estructura del informe técnico del workshop
```

## Herramientas y Versiones

- **Sistema Operativo:** Windows 64-bit (PowerShell)
- **Java JDK:** 23.0.1 (Oracle Corporation)
- **Python:** 3.14.5
- **Git:** 2.47.1.windows.2
- **Checkstyle:** *Pendiente de descarga en Paso 3*
- **PMD:** *Pendiente de descarga en Paso 3*
- **Pylint:** *Pendiente de instalación en Paso 2*
- **Flake8:** *Pendiente de instalación en Paso 2*

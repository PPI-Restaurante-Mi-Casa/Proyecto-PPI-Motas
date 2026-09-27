# Proyecto Motas - Plataforma Veterinaria

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)

Plataforma web integral desarrollada para la veterinaria **Motas** (Itagüí, Colombia). Este sistema optimiza la gestión de citas médicas, digitaliza el historial clínico de las mascotas, facilita procesos de adopción y provee una línea de asistencia para emergencias 24/7.

## Equipo de Desarrollo (Scrum)
* **Miguel Angel Higuita:** Backend Core, DevOps y Arquitectura Cloud (AWS).
* **Ximena Ruiz Flores:** Frontend, UI/UX y Gestión de Estilos.
* **Tomás Ramírez Medina:** Backend, Modelos de Base de Datos y Formularios.

## Requisitos Previos
Para ejecutar este proyecto en un entorno local, necesitas tener instalado:
* Python 3.10 o superior.
* Git.
* Pip (Gestor de paquetes de Python).

## Guía de Instalación Rápida

**1. Clonar el repositorio:**
\`\`\`bash
git clone https://github.com/PPI-Restaurante-Mi-Casa/Proyecto-PPI-Motas.git
cd Proyecto-PPI-Motas
\`\`\`

**2. Crear y activar el entorno virtual:**
\`\`\`bash
python -m venv venv
source venv/Scripts/activate  # En Windows
\`\`\`

**3. Instalar las dependencias del proyecto:**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

**4. Ejecutar las migraciones de la base de datos:**
\`\`\`bash
python manage.py makemigrations
python manage.py migrate
\`\`\`

**5. Levantar el servidor local:**
\`\`\`bash
python manage.py runserver
\`\`\`
Accede a la aplicación desde tu navegador en: `http://127.0.0.1:8000/`

## Estándares de Contribución
Este repositorio opera bajo una estricta política de protección de ramas. **No se permiten commits directos a la rama `main`.** 
Todo el equipo de desarrollo debe adherirse al estándar [Conventional Commits](https://www.conventionalcommits.org/) y utilizar el sistema de Pull Requests para la revisión de código (Code Review) previo a cualquier integración.

---
*Documentación extendida, diagramas de arquitectura y planes de migración a la nube (AWS) disponibles en la [Wiki del Repositorio](https://github.com/PPI-Restaurante-Mi-Casa/Proyecto-PPI-Motas/wiki).*

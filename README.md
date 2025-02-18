# 📖 Generador de Tests para Oposiciones con RAG

## 📌 Descripción
Este repositorio implementa un **sistema RAG (Retrieval-Augmented Generation)** diseñado para crear, actualizar y modificar automáticamente asistentes de OpenAI con documentos estructurados para generar tests en formato JSON. 

El caso práctico está enfocado en **contenido de oposiciones**, permitiendo la generación de preguntas basadas en los documentos suministrados.

## 🚀 Tecnologías utilizadas
### **[OpenAI API](https://platform.openai.com/docs/)**
  - Creación de embeddings a partir de documentos que contienen el contenido de las oposiciones.
  - Generación de preguntas tipo test basadas en el contenido suministrado.

## 📂 Estructura del proyecto
```
📁 TESTSOPOSICIONES
│── 📁 src
│   │── assistant.py    # Manejador de interacciones con OpenAI
│── .gitignore          # Archivos a ignorar en el repositorio
│── main.py             # Archivo principal (generación y consulta de tests)
│── prueba.ipynb        # Notebook para pruebas y validaciones
│── README.md           # Documentación del proyecto
│── requirements.txt    # Dependencias del proyecto
```

## 🎯 Propósito del código
Se crean asistentes en la API de OpenAI para interactuar con los documentos de oposiciones.

Mediante prompting, se instruye al asistente para generar tests sobre el contenido según una plantilla predefinida.

Los tests son devueltos en formato JSON, listos para su utilización.
## ⚙️ Instalación y Configuración
### 🔹 **1. Clonar el repositorio**
```bash
git clone https://github.com/SupernovaIa/TestOposiciones.git
cd TestOposiciones
```

### 🔹 **2. Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 🔹 **3. Configurar variables de entorno**
Crea un archivo `.env` en la raíz del proyecto con la API Key de OpenAI y el ID del asistente (si ya lo has creado y lo quieres utilizar):
```env
OPENAI_API_KEY=tu_clave_openai
ASSISTANT_ID=tu_id_assistant
```

### 🔹 **4. Generar tests**
Ejecuta el siguiente comando para obtener preguntas tipo test basadas en el contenido:
```bash
python main.py
```
Se pedirá al usuario un prompt donde se puede introducir el número de preguntas a generar o petición de consultas específicas.

Ejemplo de salida JSON:
```json
{
  "questions": [
    {
      "question": "Según la Ley 7/1985, de 2 de abril, reguladora de las bases del régimen local, ¿cuál de las siguientes competencias es considerada como competencia propia de los municipios?",
      "options": {
        "a": "La gestión de la educación pública.",
        "b": "La planificación y gestión del urbanismo.",
        "c": "La regulación del tráfico aéreo.",
        "d": "La defensa nacional."
      },
      "correct_answer": "b"
    },
    {
      "question": "En relación con la autonomía local, ¿qué condición debe cumplirse para la creación de nuevos municipios según la legislación vigente?",
      "options": {
        "a": "Deben contar con un mínimo de 2.000 habitantes.",
        "b": "Deben ser financieramente sostenibles y tener al menos 4.000 habitantes.",
        "c": "Deben ser aprobados por el Gobierno Central sin necesidad de consulta a los municipios interesados.",
        "d": "Deben ser solicitados por el Alcalde del municipio más cercano."
      },
      "correct_answer": "b"
    }
  ]
}
```


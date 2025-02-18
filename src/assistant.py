import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Configurar la clave de API
openai.api_key = os.getenv("OPENAI_API_KEY")

# ID del asistente en OpenAI
ASSISTANT_ID = os.getenv("ASSISTANT_ID")


class OpenAIAssistantManager:
    def __init__(self, name='', model='gpt-4o-mini', instructions='', tools=None, tool_resources=None, description=None, temperature=1, top_p=1):

        self.assistant_id = None
        self.object = "assistant"
        self.created_at = None
        self.name = name
        self.description = description
        self.model = model
        self.instructions = instructions
        self.tools = tools or []
        self.tool_resources = tool_resources or {}
        self.metadata = {}
        self.temperature = temperature
        self.top_p = top_p
        self.response_format = "auto"


    def create_assistant(self):
        """Crea un asistente de OpenAI si no existe ya."""
        if self.assistant_id is not None:
            raise ValueError("El asistente ya ha sido creado.")
        
        response = openai.beta.assistants.create(
            name=self.name,
            model=self.model,
            instructions=self.instructions,
            tools=self.tools,
            tool_resources=self.tool_resources,
            description=self.description,
            temperature=self.temperature,
            top_p=self.top_p
        )
        
        self.assistant_id = response.id
        self.created_at = response.created_at
        self.metadata = response.metadata
        return response


    def modify_assistant(self, name=None, model=None, instructions=None, tools=None, tool_resources=None, description=None, temperature=None, top_p=None):
        """Modifica el asistente existente."""
        if self.assistant_id is None:
            raise ValueError("El asistente no ha sido creado aún.")
        
        response = openai.beta.assistants.update(
            self.assistant_id,
            name=name or self.name,
            model=model or self.model,
            instructions=instructions or self.instructions,
            tools=tools or self.tools,
            tool_resources=tool_resources or self.tool_resources,
            description=description or self.description or '',
            temperature=temperature or self.temperature,
            top_p=top_p or self.top_p
        )
        
        self.name = response.name
        self.model = response.model
        self.instructions = response.instructions
        self.tools = response.tools
        self.tool_resources = response.tool_resources
        self.description = response.description
        self.temperature = response.temperature
        self.top_p = response.top_p
        self.metadata = response.metadata
        return response


    def delete_assistant(self):
        """Elimina el asistente de OpenAI si existe."""
        if self.assistant_id is None:
            raise ValueError("El asistente no ha sido creado aún.")
        
        response = openai.beta.assistants.delete(self.assistant_id)
        if response.get("deleted"):
            self.assistant_id = None
            self.created_at = None
        return response


    def get_assistant(self, id):
        """Recupera la información del asistente o lo obtiene si ya está creado."""
        if self.assistant_id is None:
            self.assistant_id = id
        
        response = openai.beta.assistants.retrieve(self.assistant_id)
        
        self.assistant_id = response.id
        self.object = response.object
        self.created_at = response.created_at
        self.name = response.name
        self.description = response.description
        self.model = response.model
        self.instructions = response.instructions
        self.tools = response.tools
        self.metadata = response.metadata
        self.top_p = response.top_p
        self.temperature = response.temperature
        self.response_format = response.response_format
        
        return response


    def chat(self, message):
        """Inicia una conversación con el asistente."""
        if self.assistant_id is None:
            raise ValueError("El asistente no ha sido creado aún.")
        
        thread = openai.beta.threads.create()
        openai.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=message
        )
        
        execution = openai.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=self.assistant_id
        )
        
        while True:
            status = openai.beta.threads.runs.retrieve(thread_id=thread.id, run_id=execution.id)
            if status.status == "completed":
                break
        
        messages = openai.beta.threads.messages.list(thread_id=thread.id)
        return messages.data[0].content[0].text.value
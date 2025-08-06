import subprocess
from langchain_core.language_models.llms import LLM
from langchain_core.outputs import LLMResult
from typing import Optional, List

class LlamafileLLM(LLM):
    def __init__(
        self,
        model_path: str = "llamafile",
        max_tokens: int = 512,
        temperature: float = 0.7,
        ngl: int = 9999,
        stream: bool = False,
    ):
        self.model_path = model_path
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.ngl = ngl
        self.stream = stream

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        cmd = [
            self.model_path,
            "--silent-prompt",
            "--log-disable",
            "-ngl", str(self.ngl),
            "-p", prompt,
            "-t", str(self.max_tokens),
            "--temp", str(self.temperature),
        ]

        if self.stream:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
            output = ""
            for line in process.stdout:
                print(line, end="")  # Optional: live print
                output += line
            process.wait()
            return output.strip()
        else:
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.stdout.strip()

    @property
    def _llm_type(self) -> str:
        return "llamafile"

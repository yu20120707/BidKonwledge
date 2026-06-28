from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Protocol
from urllib.parse import urlparse
from urllib import request


class LLMClient(Protocol):
    def generate(self, prompt: str) -> str:
        pass


class LLMConfigurationError(RuntimeError):
    pass


class LLMRequestConfigurationError(ValueError):
    pass


@dataclass(frozen=True)
class OpenAICompatibleLLMClient:
    api_key: str
    base_url: str
    model: str

    @classmethod
    def from_env(cls) -> "OpenAICompatibleLLMClient":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise LLMConfigurationError("OPENAI_API_KEY is required for generation")
        base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        return cls(api_key=api_key, base_url=base_url.rstrip("/"), model=model)

    @classmethod
    def from_request(
        cls,
        api_key: str,
        base_url: str | None = None,
        model: str | None = None,
    ) -> "OpenAICompatibleLLMClient":
        stripped_api_key = api_key.strip()
        if not stripped_api_key:
            raise LLMRequestConfigurationError("llm_config.api_key is required")

        active_base_url = (base_url or "https://api.openai.com/v1").strip().rstrip("/")
        parsed = urlparse(active_base_url)
        if parsed.scheme != "https" or not parsed.netloc:
            raise LLMRequestConfigurationError(
                "llm_config.base_url must be an HTTPS URL"
            )

        active_model = (model or "gpt-4o-mini").strip()
        if not active_model:
            raise LLMRequestConfigurationError("llm_config.model is required")

        return cls(
            api_key=stripped_api_key,
            base_url=active_base_url,
            model=active_model,
        )

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
        }
        data = json.dumps(payload).encode("utf-8")
        http_request = request.Request(
            f"{self.base_url}/chat/completions",
            data=data,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with request.urlopen(http_request, timeout=60) as response:
            body = json.loads(response.read().decode("utf-8"))
        return str(body["choices"][0]["message"]["content"])

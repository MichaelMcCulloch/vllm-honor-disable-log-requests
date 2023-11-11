from typing import Type

from vllm.model_executor.layers.quantized_linear.awq import AWQConfig
from vllm.model_executor.layers.quantized_linear.squeezellm import SqueezeLLMConfig
from vllm.model_executor.layers.quantized_linear.base_config import QuantizationConfig

_QUANTIZATION_CONFIG_REGISTRY = {
    "awq": AWQConfig,
    "squeezellm": SqueezeLLMConfig,
}


def get_quantization_config(quantization: str) -> Type[QuantizationConfig]:
    if quantization not in _QUANTIZATION_CONFIG_REGISTRY:
        raise ValueError(f"Invalid quantization method: {quantization}")
    return _QUANTIZATION_CONFIG_REGISTRY[quantization]


__all__ = [
    "QuantizationConfig",
    "get_quantization_config",
]

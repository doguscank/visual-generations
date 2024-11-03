from diffusers import StableDiffusionPipeline, DiffusionPipeline
import torch
from gen_ai.configs import stable_diffusion as sd_config
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Callable, Dict, List, Any
from PIL import Image
from pathlib import Path
from gen_ai.constants.task_types import TaskType


class StableDiffusionModelConfig(BaseModel):
    """
    Configuration class for Stable Diffusion.

    Parameters
    ----------
    hf_model_id : str
        The identifier of the model to use.
    device : str, optional
        The device to run the model on. Defaults to "cuda".
    task_type : TaskType, optional
        The type of task to perform. Defaults to TaskType.TEXT2IMG.
    check_nsfw : bool, optional
        Whether to check for NSFW content. Defaults to False.
    seed : int, optional
        The seed for random number generation. Defaults to -1.
    generator : torch.Generator, optional
        The generator for random number generation.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, protected_namespaces=())

    hf_model_id: Optional[str] = None
    model_path: Optional[Path] = None
    device: str = "cuda"
    task_type: TaskType = TaskType.TEXT2IMG

    check_nsfw: bool = False

    seed: Optional[int] = -1
    generator: Optional[torch.Generator] = None

    def model_post_init(self, __context) -> "StableDiffusionModelConfig":
        # Initialize the generator
        if self.seed == -1:
            self.seed = torch.seed()
        if self.generator is None:
            self.generator = torch.Generator(device=self.device)
            self.generator.manual_seed(self.seed)

        return self

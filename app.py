import json
import numpy as np
import torch
from transformers import pipeline
from diffusers import DiffusionPipeline
import base64
from io import BytesIO


class InferlessPythonModel:
  def initialize(self):
    self.generator = DiffusionPipeline.from_pretrained(
      "stabilityai/stable-diffusion-xl-base-1.0",
      torch_dtype=torch.float16,
      use_safetensors=True,
      variant="fp16",
      device_map="auto"
    )

  def infer(self, inputs):
    prompt = inputs["prompt"]
    num_inference_steps = inputs["num_inference_steps"]
    height = inputs["height"]
    width = inputs["width"]
    self. generator.enable_xformers_memory_efficient_attention()
    pipeline_output_image = self.generator(prompt, num_inference_steps=num_inference_steps, height=height, width=width, original_size=(1024, 1024), target_size=(512, 512)).images[0]
    buff = BytesIO()
    pipeline_output_image.save(buff, format="PNG")
    img_str = base64.b64encode(buff.getvalue())
    return {"generated_image_base64": img_str.decode('utf-8')}

  def finalize(self,args):
    self.generator = None
    

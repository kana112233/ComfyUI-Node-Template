import torch
import numpy as np
from PIL import Image

class ExampleNode:
    """
    一个简单的 ComfyUI 节点模板
    功能：接收一个输入值，进行某种处理，然后返回结果
    """
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        定义节点的输入参数
        """
        return {
            "required": {
                "image": ("IMAGE",),
                "int_param": ("INT", {
                    "default": 10, 
                    "min": 0, 
                    "max": 100, 
                    "step": 1,
                    "display": "number"
                }),
                "float_param": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.01,
                    "display": "slider"
                }),
                "string_param": ("STRING", {
                    "default": "Hello ComfyUI!",
                    "multiline": False,
                }),
                "choice_param": (["option1", "option2", "option3"], {
                    "default": "option1"
                }),
                "device": (["auto", "cpu", "mps", "cuda"], {
                    "default": "auto"
                }),
            },
            "optional": {
                "mask": ("MASK",),
            }
        }

    # 返回的数据类型 (对应 ComfyUI 的连接点颜色)
    RETURN_TYPES = ("IMAGE", "INT", "STRING")
    # 返回的名称
    RETURN_NAMES = ("image", "value", "text")
    # 节点执行的函数名
    FUNCTION = "process"
    # 节点在菜单中的分类
    CATEGORY = "ExampleCategory"

    def process(self, image, int_param, float_param, string_param, choice_param, device="auto", mask=None):
        """
        实际的处理逻辑
        """
        # 导入 ComfyUI 的进度条工具
        from comfy.utils import ProgressBar
        import time

        print(f"Processing image with param: {int_param}, text: {string_param}, device: {device}")
        
        # 设备选择逻辑
        if device == "auto":
            if torch.cuda.is_available():
                device = "cuda"
            elif torch.backends.mps.is_available():
                device = "mps"
            else:
                device = "cpu"
        
        print(f"Using device: {device}")
        
        # 模拟进度条
        total_steps = int_param
        pbar = ProgressBar(total_steps)
        
        # 将图像移动到指定设备 (示例)
        # 注意: ComfyUI 的 IMAGE通常就在CPU上，除非特别处理。
        # 这里演示如何转换 device
        process_device = torch.device(device)
        working_image = image.to(process_device)

        for i in range(total_steps):
            # 模拟一些计算
            time.sleep(0.01 * float_param)
            pbar.update(1)
        
        # 示例处理：简单的亮度调整并将结果转回 CPU
        processed_image = working_image * float_param
        processed_image = torch.clamp(processed_image, 0.0, 1.0).cpu()
        
        # 返回一个元组，顺序与 RETURN_TYPES 一一对应
        return (processed_image, int_param * 2, f"Processed: {string_param} ({choice_param}) on {device}")

# 节点映射字典
NODE_CLASS_MAPPINGS = {
    "ExampleNode": ExampleNode
}

# 节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "ExampleNode": "Example Template Node"
}

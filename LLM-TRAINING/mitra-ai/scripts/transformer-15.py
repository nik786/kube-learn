from transformers import pipeline

videoclassifer = pipeline(task = "video-classification", model="nateraw/videomae-base-finetuned-ucf101-subset")

videoclassifer("basketball.avi")



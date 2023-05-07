import os
import wave


import matplotlib.pyplot as plt

folder_path = "/Users/shutingxu/Downloads/illness_classify/respiratory/0"  # 替换为实际文件夹路径
total_files = 0
file_lengths = []

for filename in os.listdir(folder_path):
    if filename.endswith(".wav"):
        total_files += 1
        file_path = os.path.join(folder_path, filename)
        with wave.open(file_path, 'r') as wav_file:
            frames = wav_file.getnframes()
            rate = wav_file.getframerate()
            duration = frames / float(rate)
            file_lengths.append(duration)

print(f"Total WAV files: {total_files}")
print(f"Total length (in seconds): {sum(file_lengths)}")

# 绘制条形图
plt.bar(range(len(file_lengths)), file_lengths)
plt.title("respiratory label= 0 / WAV file lengths")
plt.xlabel("File index Total WAV files:%s" %(total_files))
plt.ylabel("Duration (seconds)")
plt.show()
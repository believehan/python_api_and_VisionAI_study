from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = Image.open("v06_data_aug/data_aug.jpg")

# 2. 이미지 조정(회전)
img_rotated = img.rotate(90)
########################## + 3가지 데이터 증강 진행해서 이미지 시각화!!
# 이미지 흑백
bw = ImageEnhance.Color(img).enhance(0.1)
# 이미지 선명도
Sharpness = ImageEnhance.Sharpness(img).enhance(17)

# 3. 결과 시각화
fig, ax = plt.subplots(2,4, figsize=(15, 10))
# 3-1. 원본 이미지 시각화
ax[0,0].imshow(img)
ax[0,0].axis('on')
ax[0,0].set_title('Original')

# 3-2. 회전 이미지 시각화
ax[0,1].imshow(img_rotated)
ax[0,1].axis('off')
ax[0,1].set_title('Rotated')

# 3-3. 흑백 이미지 시각화
ax[0,2].imshow(bw)
ax[0,2].axis('off')
ax[0,2].set_title('black-White')

# 3-4. 선명도 이미지 시각화
ax[0,3].imshow(Sharpness)
ax[0,3].axis('off')
ax[0,3].set_title('Sharpness')

plt.show()
# 4. 결과 이미지 저장
img_rotated.save("./img_rotated.jpg")
print(f"이미지 저장이 잘 됐습니다.")
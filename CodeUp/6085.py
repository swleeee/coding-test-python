# 6085 : [기초-종합] 그림 파일 저장용량 계산하기

w, h, b = map(float, input().split())
space = w*h*b/8/1024/1024

print(format(space, ".2f"), "MB")
import os

# 기본 디렉토리 설정
base_dir = "2025-CS-OS"
chapters = {
    "Chapter 01 컴퓨터 네트워크 시작하기": [
        "01-1 컴퓨터 네트워크를 알아야 하는 이유",
        "01-2 네트워크 거시적으로 살펴보기",
        "01-3 네트워크 미시적으로 살펴보기"
    ],
    "Chapter 02 물리 계층과 데이터 링크 계층": [
        "02-1 이더넷",
        "02-2 NIC와 케이블",
        "02-3 허브",
        "02-4 스위치"
    ],
    "Chapter 03 네트워크 계층": [
        "03-1 LAN을 넘어서는 네트워크 계층",
        "03-2 IP 주소",
        "03-3 라우팅"
    ],
    "Chapter 04 전송 계층": [
        "04-1 전송 계층 개요: IP의 한계와 포트",
        "04-2 TCP와 UDP",
        "04-3 TCP의 오류·흐름·혼잡 제어"
    ],
    "Chapter 05 응용 계층": [
        "05-1 DNS와 자원",
        "05-2 HTTP",
        "05-3 HTTP 헤더와 HTTP 기반 기술"
    ],
    "Chapter 06 실습으로 복습하는 네트워크": [
        "06-1 와이어샤크 설치 및 사용법",
        "06-2 와이어샤크를 통한 프로토콜 분석"
    ],
    "Chapter 07 네트워크 심화": [
        "07-1 안정성을 위한 기술",
        "07-2 안전성을 위한 기술",
        "07-3 무선 네트워크"
    ]
}

def create_study_structure(base_dir, chapters):
    os.makedirs(base_dir, exist_ok=True)
    for chapter, sections in chapters.items():
        chapter_path = os.path.join(base_dir, chapter)
        os.makedirs(chapter_path, exist_ok=True)
        for section in sections:
            section_path = os.path.join(chapter_path, section)
            os.makedirs(section_path, exist_ok=True)
            
            # 기본 README.md 생성
            readme_path = os.path.join(section_path, "README.md")
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(f"# {section}\n\n")
                f.write("## 📌 학습 목표\n- 해당 챕터의 개념 정리\n\n")
                f.write("## ❓ 확인 문제\n")
                f.write("Q1. 질문을 입력하세요.\n")
            
                f.write("## 📝 사용법  \n")
                f.write("### 이렇게 활용해 보세요! ✨  \n")
                f.write("1. ❓ 확인 문제 아래에 본인이 만든 질문을 추가하세요.  \n")
                f.write("2. 설명이 길어질 경우, 따로 마크다운 파일을 만들고 링크를 함께 추가해 주세요! 🔗  \n\n")
                f.write("### 🔗 링크 추가 방법  \n")
                f.write("1. 먼저 질문을 작성합니다.  \n")
                f.write("2. 링크를 적용할 문장을 마우스로 선택합니다.  \n")
                f.write("3. URL을 붙여넣습니다.  \n")
                f.write("4. 마크다운 형식으로 `[내용](링크)` 형태로 정리됩니다.  \n")
    print(f"✅ '{base_dir}' 디렉토리가 성공적으로 생성되었습니다!")

# 실행
test_run = True  # 실제 실행할 때는 False로 변경
if test_run:
    create_study_structure(base_dir, chapters)

import os
import shutil
import sys

def convert_py_to_txt(directory_path):
    """
    주어진 디렉토리 내의 모든 .py 파일을 .txt 파일로 복제합니다.
    
    Args:
        directory_path (str): .py 파일을 찾을 디렉토리 경로
    """
    # 경로가 유효한지 확인
    if not os.path.isdir(directory_path):
        print(f"오류: '{directory_path}'는 유효한 디렉토리가 아닙니다.")
        return

    # 디렉토리 내 모든 항목 가져오기
    try:
        files = os.listdir(directory_path)
    except Exception as e:
        print(f"디렉토리를 읽는 중 오류 발생: {e}")
        return

    # .py 파일만 필터링
    py_files = [file for file in files if file.endswith('.py')]
    
    if not py_files:
        print(f"'{directory_path}' 디렉토리에 .py 파일이 없습니다.")
        return
    
    # 각 .py 파일을 .txt 파일로 복제
    for py_file in py_files:
        py_file_path = os.path.join(directory_path, py_file)
        txt_file_name = py_file[:-3] + '.txt'  # .py 확장자를 .txt로 변경
        txt_file_path = os.path.join(directory_path, txt_file_name)
        
        try:
            # 파일 내용 복사
            shutil.copy2(py_file_path, txt_file_path)
            print(f"복제 완료: {py_file} -> {txt_file_name}")
        except Exception as e:
            print(f"{py_file} 복제 중 오류 발생: {e}")

def main():
    # 명령줄 인수로 경로 받기 또는 사용자 입력 받기
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
    else:
        directory_path = input("파이썬 파일이 있는 경로를 입력하세요: ")
    
    # 경로의 끝에 있는 슬래시 제거
    directory_path = directory_path.rstrip('\\/')
    
    # 변환 함수 실행
    convert_py_to_txt(directory_path)

if __name__ == "__main__":
    main()

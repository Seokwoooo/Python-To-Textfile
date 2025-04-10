import os
import shutil
import sys
import datetime
import glob

def convert_files_to_txt(directory_path, extensions=['.py', '.json']):
    """
    주어진 디렉토리와 하위 디렉토리 내의 모든 지정된 확장자 파일을 .txt 파일로 복제합니다.
    
    Args:
        directory_path (str): 변환할 파일을 찾을 디렉토리 경로
        extensions (list): 변환할 파일 확장자 목록 (기본값: ['.py', '.json'])
    """
    # 경로가 유효한지 확인
    if not os.path.isdir(directory_path):
        print(f"오류: '{directory_path}'는 유효한 디렉토리가 아닙니다.")
        return

    # 출력 디렉토리 생성 (python-to-textfile 폴더 내 날짜_시간 폴더)
    current_time = datetime.datetime.now()
    date_time_folder = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    output_base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "python-to-textfile")
    output_dir = os.path.join(output_base_dir, date_time_folder)
    
    # 출력 디렉토리가 없으면 생성
    os.makedirs(output_dir, exist_ok=True)
    print(f"출력 폴더 생성: {output_dir}")

    # 찾은 파일 개수 카운트
    found_files = 0
    converted_files = 0

    # 모든 하위 디렉토리 포함하여 파일 검색
    for extension in extensions:
        pattern = os.path.join(directory_path, f"**/*{extension}")
        for src_file_path in glob.glob(pattern, recursive=True):
            found_files += 1
            
            # 원본 파일 경로에서 상대 경로 구조 추출
            rel_path = os.path.relpath(src_file_path, directory_path)
            file_name = os.path.basename(src_file_path)
            sub_dir = os.path.dirname(rel_path)
            
            # 출력 파일 경로 생성
            txt_file_name = os.path.splitext(file_name)[0] + '.txt'
            
            # 출력 파일이 위치할 하위 디렉토리 생성
            dest_subdir = os.path.join(output_dir, sub_dir)
            if sub_dir and not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir, exist_ok=True)
            
            # 출력 파일 전체 경로
            txt_file_path = os.path.join(dest_subdir, txt_file_name)
            
            try:
                # 파일 내용 복사
                shutil.copy2(src_file_path, txt_file_path)
                converted_files += 1
                print(f"복제 완료: {src_file_path} -> {txt_file_path}")
            except Exception as e:
                print(f"{src_file_path} 복제 중 오류 발생: {e}")
    
    if found_files == 0:
        print(f"'{directory_path}' 디렉토리에 지정된 확장자({', '.join(extensions)})를 가진 파일이 없습니다.")
    else:
        print(f"총 {found_files}개 파일 중 {converted_files}개 파일이 성공적으로 변환되었습니다.")
        print(f"모든 파일이 '{output_dir}' 디렉토리에 저장되었습니다.")

def main():
    # 명령줄 인수로 경로 받기 또는 사용자 입력 받기
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
    else:
        directory_path = input("변환할 파일이 있는 경로를 입력하세요: ")
    
    # 경로의 끝에 있는 슬래시 제거
    directory_path = directory_path.rstrip('\\/')
    
    # 변환 함수 실행
    convert_files_to_txt(directory_path)

if __name__ == "__main__":
    main()

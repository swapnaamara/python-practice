def read_in_chunks(file_path, chunk_size=1024):
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            while True:
                data = f.read(chunk_size)  
                if not data:  
                    break
                yield data  
    except FileNotFoundError:
        print(f"Error: {file_path} ")
    except Exception as e:
        print(f"Error: {e}")


def process(chunk):
    

    print(f"Processing chunk of size: {len(chunk)} bytes")
    
    
    lines = chunk.split('\n')
    print(f"Lines in this chunk: {len(lines)}")
    
    # Example 3: Specific word search
    # if "error" in chunk.lower():
    #     print("Found 'error' in chunk")


# Usage
if __name__ == "__main__":
    file_name = "big_file.txt"
    chunk_size_bytes = 4096  # 4KB chunks
    
    total_chunks = 0
    for chunk in read_in_chunks(file_name, chunk_size_bytes):
        process(chunk)
        total_chunks += 1
    
    print(f"\nTotal chunks processed: {total_chunks}")

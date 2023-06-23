
def test_indexing_mainnet(tevm_node):
    env = {
        'LOG_LEVEL': 'debug'
    }

    env.update(os.environ)

    proc = subprocess.Popen(
        ['node', 'build/main.js'],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        encoding='utf-8',
        env=env
    )

    thread = threading.Thread(target=stream_process_output, args=(proc, message))
    thread.start()
    thread.join(timeout=timeout)

    if thread.is_alive():
        proc.terminate()
        thread.join()  # ensure the process has terminated before raising the exception
        raise ProcessTimeout(f"Process did not finish within {timeout} seconds")

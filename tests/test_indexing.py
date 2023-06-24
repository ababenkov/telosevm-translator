import os
import threading
import subprocess

from conftest import await_message_in_logs 


def test_indexing_local(tevm_node):
    await_message_in_logs(
        'switched to HEAD mode!')


def test_indexing_mainnet(tevm_node_mainnet):
    await_message_in_logs(
        'switched to HEAD mode!',
        timeout=60,
        extra_env={
            'CHAIN_ID': '40',
            'TELOS_REMOTE_ENDPOINT': 'https://mainnet.telos.net',
            'EVM_DEPLOY_BLOCK': '180698860',
            'INDEXER_START_BLOCK': '180698860'
        })

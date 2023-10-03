# -*- coding: utf-8 -*-

"""
m3u8ToMP4
~~~~~~~~~~~~

Basic usage:

import m3u8_to_mp4
m3u8_to_mp4.download("https://xxx.com/xxx/index.m3u8")


"""

import logging
import subprocess

from m3u8_To_MP4.helpers import printer_helper

printer_helper.config_logging()


# verify ffmpeg
def verify_ffmpey():
    test_has_ffmpeg_cmd = "ffmpeg -version"

    proc = subprocess.Popen(test_has_ffmpeg_cmd, shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outs, errs = proc.communicate()
    output_text = outs.decode('utf8')
    if 'version' not in output_text:
        logging.warning('NOT FOUND FFMPEG!')
        logging.info('Compressing into tar.bz2 is only supported')


# define API
import m3u8_To_MP4.multithreads_processor
from m3u8_To_MP4.v2_async_processor import AsynchronousFileCrawler
from m3u8_To_MP4.v2_async_processor import AsynchronousUriCrawler
from m3u8_To_MP4.v2_multithreads_processor import MultiThreadsFileCrawler
from m3u8_To_MP4.v2_multithreads_processor import MultiThreadsUriCrawler

__all__ = (
    "MultiThreadsFileCrawler",
    "MultiThreadsUriCrawler",
    "AsynchronousFileCrawler",
    "AsynchronousUriCrawler",
    "async_download",
    "async_file_download",
    "async_uri_download",
    "multithread_download",
    "multithread_file_download",
    "multithread_uri_download",
    "download"
)


# ================ Async ===================
def async_download(m3u8_uri, file_path='./m3u8_To_MP4.ts', customized_http_header=None, max_retry_times=3,
                   num_concurrent=50, tmpdir=None, proxy=None, tracker=None):
    '''
    Download mp4 video from given m3u uri.

    :param m3u8_uri: m3u8 uri
    :param max_retry_times: max retry times
    :param max_concurrent: concurrency
    :param mp4_file_dir: folder path where mp4 file is stored
    :param mp4_file_name: a mp4 file name with suffix ".mp4"
    :return:
    '''

    with m3u8_To_MP4.v2_async_processor.AsynchronousUriCrawler(m3u8_uri,
                                                               file_path,
                                                               customized_http_header,
                                                               max_retry_times,
                                                               num_concurrent,
                                                               tmpdir,
                                                               proxy, tracker) as crawler:
        crawler.fetch_mp4_by_m3u8_uri('ts')


def async_uri_download(m3u8_uri, file_path='./m3u8_To_MP4.mp4', customized_http_header=None,
                       max_retry_times=3, num_concurrent=50, tmpdir=None, proxy=None, tracker=None):
    with m3u8_To_MP4.v2_async_processor.AsynchronousUriCrawler(m3u8_uri,
                                                               file_path,
                                                               customized_http_header,
                                                               max_retry_times,
                                                               num_concurrent,
                                                               tmpdir,
                                                               proxy, tracker) as crawler:
        crawler.fetch_mp4_by_m3u8_uri('ts')


def async_file_download(m3u8_uri, m3u8_file_path, file_path='./m3u8_To_MP4.ts', customized_http_header=None,
                        max_retry_times=3, num_concurrent=50, tmpdir=None, proxy=None, tracker=None):
    with m3u8_To_MP4.v2_async_processor.AsynchronousFileCrawler(m3u8_uri,
                                                                m3u8_file_path,
                                                                file_path,
                                                                customized_http_header,
                                                                max_retry_times,
                                                                num_concurrent,
                                                                tmpdir,
                                                                proxy, tracker) as crawler:
        crawler.fetch_mp4_by_m3u8_uri('ts')


# ================ MultiThread ===================
def multithread_download(m3u8_uri, file_path='./m3u8_To_MP4.mp4', customized_http_header=None,
                         max_retry_times=3, max_num_workers=100, tmpdir=None, proxy=None, tracker=None):
    '''
    Download mp4 video from given m3u uri.

    :param m3u8_uri: m3u8 uri
    :param file_path: mp4 file path
    :param customized_http_header: headers that may be required to download the m3u8
    :param max_retry_times: max retry times
    :param max_num_workers: number of download threads
    
    :return:
    '''
    with m3u8_To_MP4.v2_multithreads_processor.MultiThreadsUriCrawler(m3u8_uri,
                                                                      file_path,
                                                                      customized_http_header,
                                                                      max_retry_times,
                                                                      max_num_workers,
                                                                      tmpdir,
                                                                      proxy, tracker) as crawler:
        crawler.fetch_mp4_by_m3u8_uri('ts')


def multithread_uri_download(m3u8_uri, file_path='./m3u8_To_MP4.ts', customied_http_header=None,
                             max_retry_times=3, max_num_workers=100, tmpdir=None, proxy=None, tracker=None):
    with m3u8_To_MP4.v2_multithreads_processor.MultiThreadsUriCrawler(m3u8_uri,
                                                                      file_path,
                                                                      customied_http_header,
                                                                      max_retry_times,
                                                                      max_num_workers,
                                                                      tmpdir,
                                                                      proxy, tracker) as crawler:
        crawler.fetch_mp4_by_m3u8_uri('ts')


def multithread_file_download(m3u8_uri, m3u8_file_path, file_path,
                              customized_http_header=None, max_retry_times=3,
                              max_num_workers=100, tmpdir=None, proxy=None, tracker=None):
    with m3u8_To_MP4.v2_multithreads_processor.MultiThreadsFileCrawler(
            m3u8_uri, m3u8_file_path, file_path, customized_http_header, max_retry_times,
            max_num_workers, tmpdir, proxy, tracker) as crawler:
        crawler.fetch_mp4_by_m3u8_uri(True)


# ================ Deprecated Function ===================
import warnings


def download(m3u8_uri, max_retry_times=3, max_num_workers=100,
             mp4_file_dir='./', mp4_file_name='m3u8_To_MP4', tmpdir=None):
    '''
    Download mp4 video from given m3u uri.

    :param m3u8_uri: m3u8 uri
    :param max_retry_times: max retry times
    :param max_num_workers: number of download threads
    :param mp4_file_dir: folder path where mp4 file is stored
    :param mp4_file_name: a mp4 file name with suffix ".mp4"
    :return:
    '''
    warnings.warn(
            'download function is deprecated, and please use multithread_download.',
            DeprecationWarning)

    with m3u8_To_MP4.multithreads_processor.Crawler(m3u8_uri, max_retry_times,
                                                    max_num_workers,
                                                    mp4_file_dir,
                                                    mp4_file_name,
                                                    tmpdir) as crawler:
        crawler.fetch_mp4_by_m3u8_uri()

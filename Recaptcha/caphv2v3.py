import asyncio
import logging
import logging.config
import os
import random
import sys
import threading

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'CRITICAL',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'my_app': {
            'level': 'CRITICAL',
            'handlers': ['console'],
			'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)

from uuid import uuid4
from concurrent.futures import ProcessPoolExecutor

from fastapi import FastAPI, Request, Response
from fastapi.responses import PlainTextResponse
from playwright.async_api import async_playwright
from playwright_recaptcha import (
    CapSolverError,
    RecaptchaNotFoundError,
    RecaptchaRateLimitError,
    RecaptchaTimeoutError,
    RecaptchaSolveError,
    RecaptchaError,
    recaptchav2,
    recaptchav3
)

from datetime import datetime, timedelta
from time import sleep
from queue import Queue

sys.stderr = open("caphv2v3_err.log", "w")

############################################################################
# Constants
############################################################################

max_workers_pool_executor = 5

trys_connection = 3

interval_in_seconds_new_random_proxy_h = 300
interval_in_seconds_new_random_proxy_v2 = 300
interval_in_seconds_new_random_proxy_v3 = 300

is_providing_stat_h = False
is_providing_stat_v2a = True
is_providing_stat_v2ic = True
is_providing_stat_v3 = True

is_logging = True

is_logging_worked_proxy_h = True
is_logging_worked_proxy_v2 = True
is_logging_worked_proxy_v3 = True

is_logging_failed_proxy_h = True
is_logging_failed_proxy_v2 = True
is_logging_failed_proxy_v3 = True

is_deleting_failed_rotating_proxy_h = False
is_deleting_failed_rotating_proxy_v2 = False
is_deleting_failed_rotating_proxy_v3 = False

filename_proxy_h = './proxy/randoming_proxy_data_h.txt'
filename_proxy_v2 = './proxy/randoming_proxy_data_v2.txt'
filename_proxy_v3 = './proxy/randoming_proxy_data_v3.txt'

filename_rotating_proxy_h = './proxy/rotating_proxy_data_h.txt'
filename_rotating_proxy_v2 = './proxy/rotating_proxy_data_v2.txt'
filename_rotating_proxy_v3 = './proxy/rotating_proxy_data_v3.txt'

filename_worked_proxy_h = './proxy/worked_proxy_data_h.txt'
filename_worked_proxy_v2 = './proxy/worked_proxy_data_v2.txt'
filename_worked_proxy_v3 = './proxy/worked_proxy_data_v3.txt'

filename_failed_proxy_h = './proxy/failed_proxy_data_h.txt'
filename_failed_proxy_v2 = './proxy/failed_proxy_data_v2.txt'
filename_failed_proxy_v3 = './proxy/failed_proxy_data_v3.txt'

filename_log_h = './log/log_h.txt'
filename_log_v2 = './log/log_v2.txt'
filename_log_v3 = './log/log_v3.txt'

filename_stat_h = './stat/stat_h.txt'
filename_stat_v2a = './stat/stat_v2a.txt'
filename_stat_v2ic = './stat/stat_v2ic.txt'
filename_stat_v3 = './stat/stat_v3.txt'

filename_stat_temp = './temp/stat_temp.txt'

timeout_in_milliseconds_solver_v2a = 60000
timeout_in_milliseconds_solver_v2ic = 60000
timeout_in_milliseconds_solver_v3 = 60000

timeout_in_seconds_aborting_thread_h = 120
timeout_in_seconds_aborting_thread_v2a = 120
timeout_in_seconds_aborting_thread_v2ic = 120
timeout_in_seconds_aborting_thread_v3 = 120

############################################################################
# Init
############################################################################

app = FastAPI()
executor = ProcessPoolExecutor(max_workers=max_workers_pool_executor)
q_stat = Queue()

############################################################################
# Stats by solving
############################################################################

class c_stat_hv2v3:

	############################################################################
	# RECAPTCHA V2 (AUDIO)
	############################################################################

    RECAPTCHAV2_AUDIO = 0
    TRYS_RECAPTCHAV2_AUDIO = 0
    TRY1_RECAPTCHAV2_AUDIO = 0
    TRY2_RECAPTCHAV2_AUDIO = 0
    TRY3_RECAPTCHAV2_AUDIO = 0
    SUCCESS_RECAPTCHAV2_AUDIO = 0
    ERROR_RECAPTCHAV2_AUDIO_NOT_FOUND = 0
    ERROR_RECAPTCHAV2_AUDIO_RATE_LIMIT = 0
    ERROR_RECAPTCHAV2_AUDIO_SOLVE = 0
    ERROR_RECAPTCHAV2_AUDIO = 0
    ERROR_RECAPTCHAV2_AUDIO_EXCEPTION = 0
    ERROR_CONNECTION_RECAPTCHAV2_AUDIO = 0
    ABORT_TIMEOUT_RECAPTCHAV2_AUDIO = 0
    EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_AUDIO = 0

	############################################################################
	# RECAPTCHA V2 (IMAGE CHALLENGE)
	############################################################################

    RECAPTCHAV2_IMAGE_CHALLENGE = 0
    TRYS_RECAPTCHAV2_IMAGE_CHALLENGE = 0
    TRY1_RECAPTCHAV2_IMAGE_CHALLENGE = 0
    TRY2_RECAPTCHAV2_IMAGE_CHALLENGE = 0
    TRY3_RECAPTCHAV2_IMAGE_CHALLENGE = 0
    SUCCESS_RECAPTCHAV2_IMAGE_CHALLENGE = 0
    ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_CAP_SOLVER = 0
    ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_NOT_FOUND = 0
    ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_RATE_LIMIT = 0
    ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_SOLVE = 0
    ERROR_RECAPTCHAV2_IMAGE_CHALLENGE = 0
    ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_EXCEPTION = 0
    ERROR_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE = 0
    ABORT_TIMEOUT_RECAPTCHAV2_IMAGE_CHALLENGE = 0
    EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_IMAGE_CHALLENGE = 0

	############################################################################
	# RECAPTCHA V3
	############################################################################

    RECAPTCHAV3 = 0
    TRYS_RECAPTCHAV3 = 0
    TRY1_RECAPTCHAV3 = 0
    TRY2_RECAPTCHAV3 = 0
    TRY3_RECAPTCHAV3 = 0
    SUCCESS_RECAPTCHAV3 = 0
    ERROR_RECAPTCHAV3_NOT_FOUND = 0
    ERROR_RECAPTCHAV3_RATE_LIMIT = 0
    ERROR_RECAPTCHAV3_SOLVE = 0
    ERROR_RECAPTCHAV3 = 0
    ERROR_RECAPTCHAV3_EXCEPTION = 0
    ERROR_CONNECTION_RECAPTCHAV3 = 0
    ABORT_TIMEOUT_RECAPTCHAV3 = 0
    EXCEPTION_LOOP_SOLVING_RECAPTCHAV3 = 0
	
	############################################################################
	# HCAPTCHA
	############################################################################

    HCAPTCHA = 0
    TRYS_HCAPTCHA = 0
    TRY1_HCAPTCHA = 0
    TRY2_HCAPTCHA = 0
    TRY3_HCAPTCHA = 0
    SUCCESS_HCAPTCHA = 0
    ERROR_CONNECTION_HCAPTCHA = 0
    ABORT_TIMEOUT_HCAPTCHA = 0
    EXCEPTION_LOOP_SOLVING_HCAPTCHA = 0

############################################################################
# Init
############################################################################

@app.on_event("startup")
async def startup_event():
	clean_files()
		
############################################################################
# To trigger the SOLVING
############################################################################

async def solve_captchav2_audio(page_url: str, ran_id: str, task_abort: threading.Thread, stat_hv2v3: c_stat_hv2v3) -> str:
    async with async_playwright() as playwright:

        stat_hv2v3.RECAPTCHAV2_AUDIO = int(stat_hv2v3.RECAPTCHAV2_AUDIO) + 1

        error_connection = False
        try_connection = 0
        force_new_proxy = False

        proxy = 'NO_PROXY'

        while ((try_connection == 0) or ((try_connection <= trys_connection) and error_connection)):
            task_abort.resetTempo()

            stat_hv2v3.TRYS_RECAPTCHAV2_AUDIO = int(stat_hv2v3.TRYS_RECAPTCHAV2_AUDIO) + 1

            error_connection = False
            try_connection = try_connection + 1

            if try_connection == 1:
                stat_hv2v3.TRY1_RECAPTCHAV2_AUDIO = int(stat_hv2v3.TRY1_RECAPTCHAV2_AUDIO) + 1
            if try_connection == 2:
                stat_hv2v3.TRY2_RECAPTCHAV2_AUDIO = int(stat_hv2v3.TRY2_RECAPTCHAV2_AUDIO) + 1
            if try_connection == 3:
                stat_hv2v3.TRY3_RECAPTCHAV2_AUDIO = int(stat_hv2v3.TRY3_RECAPTCHAV2_AUDIO) + 1
				
            proxy = await get_proxy_v2(force_new_proxy)
            force_new_proxy = False

            try:
                if proxy == 'NO_PROXY':
                    await print_async(f'NEW SOLVING RECAPTCHA v2 (AUDIO) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={proxy}')
                    if is_logging:
                        await log_async_v2(f'NEW SOLVING RECAPTCHA v2 (AUDIO) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={proxy}')

                    browser = await playwright.firefox.launch(slow_mo=3000)
                else:
                    data = proxy.split(':')
                    if len(data) == 4:
                        host = data[0] + ':' + data[1]
                        usr = data[2]
                        pwd = data[3]

                        await print_async(f'NEW SOLVING RECAPTCHA v2 (AUDIO) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}|{usr}|{pwd}')
                        if is_logging:
                            await log_async_v2(f'NEW SOLVING RECAPTCHA v2 (AUDIO) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}|{usr}|{pwd}')

                        browser = await playwright.firefox.launch(headless=True, proxy={"server" : host,"username" : usr,"password" : pwd})
                    else:
                        host = data[0] + ':' + data[1]

                        await print_async(f'NEW SOLVING RECAPTCHA v2 (AUDIO) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}')
                        if is_logging:
                            await log_async_v2(f'NEW SOLVING RECAPTCHA v2 (AUDIO) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}')	

                        browser = await playwright.firefox.launch(headless=True, proxy={"server" : host})
                            
                page = await browser.new_page()
                await page.goto(page_url, wait_until="networkidle")
                
            except Exception as e:
                if not page.is_closed():
                    await page.close()
                await browser.close()

                await print_async(f'CONNECTION RECAPTCHA v2 (AUDIO) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'PROXY={proxy}',f'EXCEPTION={e}')
                if is_logging:
                    await log_async_v2(f'CONNECTION RECAPTCHA v2 (AUDIO) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'PROXY={proxy}',f'EXCEPTION={e}')

                error_connection = True

                if e != 'SSL_ERROR_BAD_CERT_DOMAIN':
                    if e != 'SEC_ERROR_UNKNOWN_ISSUER':
                        if e != 'SEC_ERROR_UNKNOWN':
                            if e != 'SEC_ERROR_EXPIRED_CERTIFICATE':
                                if try_connection == 3:
                                    try_connection = 1
                                    force_new_proxy = True

                                    if proxy != 'NO_PROXY':
                                        if is_logging_failed_proxy_v2:
                                            await add_failed_proxy_v2(f'{proxy}')

                                            await print_async(f'NEW FAILED PROXY RECAPTCHA v2 (AUDIO) - PROXY={proxy}','','','')
                                            if is_logging:
                                                await log_async_v2(f'NEW FAILED PROXY RECAPTCHA v2 (AUDIO) - PROXY={proxy}','','','')

                                        if is_deleting_failed_rotating_proxy_v2:
                                            await delete_rotating_proxy_v2(proxy)

        if error_connection:
            stat_hv2v3.ERROR_CONNECTION_RECAPTCHAV2_AUDIO = int(stat_hv2v3.ERROR_CONNECTION_RECAPTCHAV2_AUDIO) + 1

            await print_async(f'CONNECTION RECAPTCHA v2 (AUDIO) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'PROXY={proxy}','EXCEPTION=ERROR_NO_CONNECTION_RECAPTCHAV2_AUDIO')

            return 'ERROR_NO_CONNECTION_RECAPTCHAV2_AUDIO'
        else:
            if proxy != 'NO_PROXY':
                if is_logging_worked_proxy_v2:
                    await add_worked_proxy_v2(f'{proxy}')

                    await print_async(f'NEW WORKED PROXY RECAPTCHA v2 (AUDIO) - PROXY={proxy}','','','')
                    if is_logging:
                        await log_async_v2(f'NEW WORKED PROXY RECAPTCHA v2 (AUDIO) - PROXY={proxy}','','','')
									
        try:
	    #async with recaptchav2.AsyncSolver(page, timeout=timeout_in_milliseconds_solver_v2a) as solver:
            solver = recaptchav2.AsyncSolver(page)
            token = await solver.solve_recaptcha(wait=True)
            solver.close()

            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.SUCCESS_RECAPTCHAV2_AUDIO = int(stat_hv2v3.SUCCESS_RECAPTCHAV2_AUDIO) + 1

            return f'OK|{token}'
        except RecaptchaNotFoundError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO_NOT_FOUND = int(stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO_NOT_FOUND) + 1

            return f'ERROR_RECAPTCHAV2_AUDIO_NOT_FOUND={e}'
        except RecaptchaRateLimitError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO_RATE_LIMIT = int(stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO_RATE_LIMIT) + 1

            return f'ERROR_RECAPTCHAV2_AUDIO_RATE_LIMIT={e}'
        except RecaptchaSolveError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO_SOLVE = int(stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO_SOLVE) + 1

            return f'ERROR_RECAPTCHAV2_AUDIO_SOLVE={e}'
        except RecaptchaError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO = int(stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO) + 1

            return f'ERROR_RECAPTCHAV2_AUDIO={e}'
        except Exception as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO_EXCEPTION = int(stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO_EXCEPTION) + 1

            return f'ERROR_RECAPTCHAV2_AUDIO_EXCEPTION={e}'

async def solve_captchav2_image_challenge(page_url: str, ran_id: str, my_cap_solver_api_key: str, task_abort: threading.Thread, stat_hv2v3: c_stat_hv2v3) -> str:
    async with async_playwright() as playwright:
		
        stat_hv2v3.RECAPTCHAV2_IMAGE_CHALLENGE = int(stat_hv2v3.RECAPTCHAV2_IMAGE_CHALLENGE) + 1

        error_connection = False
        try_connection = 0
        force_new_proxy = False

        proxy = 'NO_PROXY'

        while ((try_connection == 0) or ((try_connection <= trys_connection) and error_connection)):
            task_abort.resetTempo()

            stat_hv2v3.TRYS_RECAPTCHAV2_IMAGE_CHALLENGE = int(stat_hv2v3.TRYS_RECAPTCHAV2_IMAGE_CHALLENGE) + 1

            error_connection = False
            try_connection = try_connection + 1
			
            if try_connection == 1:
                stat_hv2v3.RY1_RECAPTCHAV2_IMAGE_CHALLENGE = int(stat_hv2v3.TRY1_RECAPTCHAV2_IMAGE_CHALLENGE) + 1
            if try_connection == 2:
                stat_hv2v3.TRY2_RECAPTCHAV2_IMAGE_CHALLENGE = int(stat_hv2v3.TRY2_RECAPTCHAV2_IMAGE_CHALLENGE) + 1
            if try_connection == 3:
                stat_hv2v3.TRY3_RECAPTCHAV2_IMAGE_CHALLENGE = int(stat_hv2v3.TRY3_RECAPTCHAV2_IMAGE_CHALLENGE) + 1
				
            proxy = await get_proxy_v2(force_new_proxy)
            force_new_proxy = False

            try:	
                if proxy == 'NO_PROXY':
                    await print_async(f'NEW SOLVING RECAPTCHA v2 (IMAGE CHALLENGE) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={proxy}')
                    if is_logging:
                        await log_async_v2(f'NEW SOLVING RECAPTCHA v2 (IMAGE CHALLENGE) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={proxy}')

                    browser = await playwright.firefox.launch(slow_mo=3000)
                else:
                    data = proxy.split(':')
                    if len(data) == 4:
                        host = data[0] + ':' + data[1]
                        usr = data[2]
                        pwd = data[3]

                        await print_async(f'NEW SOLVING RECAPTCHA v2 (IMAGE CHALLENGE) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}|{usr}|{pwd}')
                        if is_logging:
                            await log_async_v2(f'NEW SOLVING RECAPTCHA v2 (IMAGE CHALLENGE) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}|{usr}|{pwd}')	

                        browser = await playwright.firefox.launch(headless=True, proxy={"server" : host,"username" : usr,"password" : pwd})
                    else:
                        host = data[0] + ':' + data[1]

                        await print_async(f'NEW SOLVING RECAPTCHA v2 (IMAGE CHALLENGE) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}')
                        if is_logging:
                            await log_async_v2(f'NEW SOLVING RECAPTCHA v2 (IMAGE CHALLENGE) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}')	

                        browser = await playwright.firefox.launch(headless=True, proxy={"server" : host})
                            
                page = await browser.new_page()
                await page.goto(page_url, wait_until="networkidle")
		
            except Exception as e:
                if not page.is_closed():
                    await page.close()
                await browser.close()

                await print_async(f'CONNECTION RECAPTCHA v2 (IMAGE CHALLENGE) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'PROXY={proxy}',f'EXCEPTION={e}')
                if is_logging:
                    await log_async_v2(f'CONNECTION RECAPTCHA v2 (IMAGE CHALLENGE) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'PROXY={proxy}',f'EXCEPTION={e}')
  
                error_connection = True

                if e != 'SSL_ERROR_BAD_CERT_DOMAIN':
                    if e != 'SEC_ERROR_UNKNOWN_ISSUER':
                        if e != 'SEC_ERROR_UNKNOWN':
                            if e != 'SEC_ERROR_EXPIRED_CERTIFICATE':
                                if try_connection == 3:
                                    try_connection = 1
                                    force_new_proxy = True

                                    if proxy != 'NO_PROXY':
                                        if is_logging_failed_proxy_v2:
                                            await add_failed_proxy_v2(f'{proxy}')

                                            await print_async(f'NEW FAILED PROXY RECAPTCHA v2 (IMAGE CHALLENGE) - PROXY={proxy}','','','')
                                            if is_logging:
                                                await log_async_v2(f'NEW FAILED PROXY RECAPTCHA v2 (IMAGE CHALLENGE) - PROXY={proxy}','','','')

                                        if is_deleting_failed_rotating_proxy_v2:
                                            await delete_rotating_proxy_v2(proxy)

        if error_connection:
            stat_hv2v3.ERROR_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE = int(stat_hv2v3.ERROR_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE) + 1

            await print_async(f'CONNECTION RECAPTCHA v2 (IMAGE CHALLENGE) - CONNECT_TRY={try_connection}',f'URL={page_url}',f'PROXY={proxy}','EXCEPTION=ERROR_NO_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE')

            return 'ERROR_NO_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE'
        else:
            if proxy != 'NO_PROXY':
                if is_logging_worked_proxy_v2:
                    await add_worked_proxy_v2(f'{proxy}')

                    await print_async(f'NEW WORKED PROXY RECAPTCHA v2 (IMAGE CHALLENGE) - PROXY={proxy}','','','')
                    if is_logging:
                        await log_async_v2(f'NEW WORKED PROXY RECAPTCHA v2 (IMAGE CHALLENGE) - PROXY={proxy}','','','')
						
        try:
			#async with recaptchav2.AsyncSolver(page, timeout=timeout_in_milliseconds_solver_v2ic) as solver:
            solver = recaptchav2.AsyncSolver(page)
            token = await solver.solve_recaptcha(wait=True, image_challenge=True, capsolver_api_key=my_cap_solver_api_key)
            solver.close()

            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.SUCCESS_RECAPTCHAV2_IMAGE_CHALLENGE = int(stat_hv2v3.SUCCESS_RECAPTCHAV2_IMAGE_CHALLENGE) + 1

            return f'OK|{token}'
        except CapSolverError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_CAP_SOLVER = int(stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_CAP_SOLVER) + 1

            return f'ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_CAP_SOLVER={e}'
        except RecaptchaNotFoundError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_NOT_FOUND = int(stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_NOT_FOUND) + 1

            return f'ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_NOT_FOUND={e}'
        except RecaptchaRateLimitError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_RATE_LIMIT = int(stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_RATE_LIMIT) + 1

            return f'ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_RATE_LIMIT={e}'
        except RecaptchaSolveError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_SOLVE = int(stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_SOLVE) + 1

            return f'ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_SOLVE={e}'
        except RecaptchaError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE = int(stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE) + 1

            return f'ERROR_RECAPTCHAV2_IMAGE_CHALLENGE={e}'
        except Exception as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_EXCEPTION = int(stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_EXCEPTION) + 1

            return f'ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_EXCEPTION={e}'

async def solve_captchav3(page_url: str, ran_id: str, task_abort: threading.Thread, stat_hv2v3: c_stat_hv2v3) -> str:
    async with async_playwright() as playwright:

        stat_hv2v3.RECAPTCHAV3 = int(stat_hv2v3.RECAPTCHAV3) + 1

        error_connection = False
        try_connection = 0
        force_new_proxy = False

        proxy = 'NO_PROXY'

        while ((try_connection == 0) or ((try_connection <= trys_connection) and error_connection)):
            task_abort.resetTempo()

            stat_hv2v3.TRYS_RECAPTCHAV3 = int(stat_hv2v3.TRYS_RECAPTCHAV3) + 1

            error_connection = False
            try_connection = try_connection + 1

            if try_connection == 1:
                stat_hv2v3.TRY1_RECAPTCHAV3 = int(stat_hv2v3.TRY1_RECAPTCHAV3) + 1
            if try_connection == 2:
                stat_hv2v3.TRY2_RECAPTCHAV3 = int(stat_hv2v3.TRY2_RECAPTCHAV3) + 1
            if try_connection == 3:
                stat_hv2v3.TRY3_RECAPTCHAV3 = int(stat_hv2v3.TRY3_RECAPTCHAV3) + 1

            proxy = await get_proxy_v3(force_new_proxy)
            force_new_proxy = False

            try:	
                if proxy == 'NO_PROXY':
                    await print_async(f'NEW SOLVING RECAPTCHA v3 - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={proxy}')
                    if is_logging:
                        await log_async_v3(f'NEW SOLVING RECAPTCHA v3 - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={proxy}')

                    browser = await playwright.firefox.launch(slow_mo=3000)
                else:
                    data = proxy.split(':')
                    if len(data) == 4:
                        host = data[0] + ':' + data[1]
                        usr = data[2]
                        pwd = data[3]

                        await print_async(f'NEW SOLVING RECAPTCHA v3 - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}|{usr}|{pwd}')
                        if is_logging:
                            await log_async_v3(f'NEW SOLVING RECAPTCHA v3 - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}|{usr}|{pwd}')	

                        browser = await playwright.firefox.launch(headless=True, proxy={"server" : host,"username" : usr,"password" : pwd})
                    else:
                        host = data[0] + ':' + data[1]

                        await print_async(f'NEW SOLVING RECAPTCHA v3 - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}')
                        if is_logging:
                            await log_async_v3(f'NEW SOLVING RECAPTCHA v3 - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}')	
                        
                        browser = await playwright.firefox.launch(headless=True, proxy={"server" : host})
                        
                page = await browser.new_page()
                await page.goto(page_url, wait_until="networkidle")
                
            except Exception as e:
                if not page.is_closed():
                    await page.close()
                await browser.close()

                await print_async(f'CONNECTION RECAPTCHA v3 - CONNECT_TRY={try_connection}',f'URL={page_url}',f'PROXY={proxy}',f'EXCEPTION={e}')
                if is_logging:
                    await log_async_v3(f'CONNECTION RECAPTCHA v3 - CONNECT_TRY={try_connection}',f'URL={page_url}',f'PROXY={proxy}',f'EXCEPTION={e}')
 
                error_connection = True

                if e != 'SSL_ERROR_BAD_CERT_DOMAIN':
                    if e != 'SEC_ERROR_UNKNOWN_ISSUER':
                        if e != 'SEC_ERROR_UNKNOWN':
                            if e != 'SEC_ERROR_EXPIRED_CERTIFICATE':
                                if try_connection == 3:
                                    try_connection = 1
                                    force_new_proxy = True

                                    if proxy != 'NO_PROXY':
                                        if is_logging_failed_proxy_v3:
                                            await add_failed_proxy_v3(f'{proxy}')

                                            await print_async(f'NEW FAILED PROXY RECAPTCHA v3 - PROXY={proxy}','','','')
                                            if is_logging:
                                                await log_async_v3(f'NEW FAILED PROXY RECAPTCHA v3 - PROXY={proxy}','','','')

                                        if is_deleting_failed_rotating_proxy_v3:
                                            await delete_rotating_proxy_v3(proxy)

        if error_connection:
            stat_hv2v3.ERROR_CONNECTION_RECAPTCHAV3 = int(stat_hv2v3.ERROR_CONNECTION_RECAPTCHAV3) +1

            await print_async(f'CONNECTION RECAPTCHA v3 - CONNECT_TRY={try_connection}',f'URL={page_url}',f'PROXY={proxy}','EXCEPTION=ERROR_NO_CONNECTION_RECAPTCHAV3')

            return 'ERROR_NO_CONNECTION_RECAPTCHAV3'
        else:
            if proxy != 'NO_PROXY':
                if is_logging_worked_proxy_v3:
                    await add_worked_proxy_v3(f'{proxy}')

                    await print_async(f'NEW WORKED PROXY RECAPTCHA v3 - PROXY={proxy}','','','')
                    if is_logging:
                        await log_async_v3(f'NEW WORKED PROXY RECAPTCHA v3 - PROXY={proxy}','','','')
        
        try:
            solver = recaptchav3.AsyncSolver(page, timeout=timeout_in_milliseconds_solver_v3)
            token = await solver.solve_recaptcha()
            solver.close()

            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.SUCCESS_RECAPTCHAV3 = int(stat_hv2v3.SUCCESS_RECAPTCHAV3) + 1

            return f'OK|{token}'
        except RecaptchaNotFoundError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV3_NOT_FOUND = int(stat_hv2v3.ERROR_RECAPTCHAV3_NOT_FOUND) + 1

            return f'ERROR_RECAPTCHAV3_NOT_FOUND={e}'
        except RecaptchaRateLimitError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV3_RATE_LIMIT = int(stat_hv2v3.ERROR_RECAPTCHAV3_RATE_LIMIT) + 1

            return f'ERROR_RECAPTCHAV3_RATE_LIMIT={e}'
        except RecaptchaSolveError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV3_SOLVE = int(stat_hv2v3.ERROR_RECAPTCHAV3_SOLVE) + 1

            return f'ERROR_RECAPTCHAV3_SOLVE={e}'
        except RecaptchaError as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV3 = int(stat_hv2v3.ERROR_RECAPTCHAV3) + 1

            return f'ERROR_RECAPTCHAV3={e}'
        except Exception as e:
            solver.close()
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_RECAPTCHAV3_EXCEPTION = int(stat_hv2v3.ERROR_RECAPTCHAV3_EXCEPTION) + 1

            return f'ERROR_RECAPTCHAV3_EXCEPTION={e}'

async def solve_hcaptcha(page_url: str, ran_id: str, task_abort: threading.Thread, stat_hv2v3: c_stat_hv2v3) -> str:
    async with async_playwright() as playwright:

        stat_hv2v3.HCAPTCHA = int(stat_hv2v3.HCAPTCHA) + 1

        error_connection = False
        try_connection = 0
        force_new_proxy = False

        proxy = 'NO_PROXY'

        while ((try_connection == 0) or ((try_connection <= trys_connection) and error_connection)):
            task_abort.resetTempo()

            stat_hv2v3.TRYS_HCAPTCHA = int(stat_hv2v3.TRYS_HCAPTCHA) + 1
			
            error_connection = False
            try_connection = try_connection + 1

            if try_connection == 1:
                stat_hv2v3.TRY1_HCAPTCHA = int(stat_hv2v3.TRY1_HCAPTCHA) + 1
            if try_connection == 2:
                stat_hv2v3.TRY2_HCAPTCHA = int(stat_hv2v3.TRY2_HCAPTCHA) + 1
            if try_connection == 3:
                stat_hv2v3.TRY3_HCAPTCHA = int(stat_hv2v3.TRY3_HCAPTCHA) + 1

            proxy = await get_proxy_h(force_new_proxy)
            force_new_proxy = False

            try:	
                if proxy == 'NO_PROXY':
                    await print_async(f'NEW SOLVING HCAPTCHA - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={proxy}')	
                    if is_logging:
                        await log_async_h(f'NEW SOLVING HCAPTCHA - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={proxy}')

                    browser = await playwright.firefox.launch(slow_mo=3000)
                else:
                    data = proxy.split(':')
                    if len(data) == 4:
                        host = data[0] + ':' + data[1]
                        usr = data[2]
                        pwd = data[3]

                        await print_async(f'NEW SOLVING HCAPTCHA - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}|{usr}|{pwd}')
                        if is_logging:
                            await log_async_h(f'NEW SOLVING HCAPTCHA - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}|{usr}|{pwd}')	

                        browser = await playwright.firefox.launch(headless=True, proxy={"server" : host,"username" : usr,"password" : pwd})
                    else:
                        host = data[0] + ':' + data[1]

                        await print_async(f'NEW SOLVING HCAPTCHA - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}')
                        if is_logging:
                            await log_async_h(f'NEW SOLVING HCAPTCHA - CONNECT_TRY={try_connection}',f'URL={page_url}',f'ID={ran_id}',f'PROXY={host}')	
                        
                        browser = await playwright.firefox.launch(headless=True, proxy={"server" : host})
                        
                page = await browser.new_page()
                await page.goto(page_url, wait_until="networkidle")
                
            except Exception as e:
                if not page.is_closed():
                    await page.close()
                await browser.close()

                await print_async(f'CONNECTION HCAPTCHA - CONNECT_TRY={try_connection}',f'URL={page_url}',f'PROXY={proxy}',f'EXCEPTION={e}')
                if is_logging:
                    await log_async_h(f'CONNECTION HCAPTCHA - CONNECT_TRY={try_connection}',f'URL={page_url}',f'PROXY={proxy}',f'EXCEPTION={e}')
 
                if e != 'SSL_ERROR_BAD_CERT_DOMAIN':
                    if e != 'SEC_ERROR_UNKNOWN_ISSUER':
                        if e != 'SEC_ERROR_UNKNOWN':
                            if e != 'SEC_ERROR_EXPIRED_CERTIFICATE':
                                if try_connection == 3:
                                    try_connection = 1
                                    force_new_proxy = True

                                    if proxy != 'NO_PROXY':
                                        if is_logging_failed_proxy_h:
                                            await add_failed_proxy_h(f'{proxy}')

                                            await print_async(f'NEW FAILED PROXY HCAPTCHA - PROXY={proxy}','','','')
                                            if is_logging:
                                                await log_async_h(f'NEW FAILED PROXY HCAPTCHA - PROXY={proxy}','','','')

                                        if is_deleting_failed_rotating_proxy_h:
                                            await delete_rotating_proxy_h(proxy)

        if error_connection:
            stat_hv2v3.ERROR_CONNECTION_HCAPTCHA = int(stat_hv2v3.ERROR_CONNECTION_HCAPTCHA) +1

            await print_async(f'CONNECTION HCAPTCHA - CONNECT_TRY={try_connection}',f'URL={page_url}',f'PROXY={proxy}','EXCEPTION=ERROR_NO_CONNECTION_HCAPTCHA')

            return 'ERROR_NO_CONNECTION_HCAPTCHA'
        else:
            if proxy != 'NO_PROXY':
                if is_logging_worked_proxy_h:
                    await add_worked_proxy_h(f'{proxy}')

                    await print_async(f'NEW WORKED PROXY HCAPTCHA - PROXY={proxy}','','','')
                    if is_logging:
                        await log_async_h(f'NEW WORKED PROXY HCAPTCHA - PROXY={proxy}','','','','')

#######################################################################################
### https://pypi.org/project/hcaptcha-solver/
#######################################################################################

#from hcaptcha_solver import hcaptcha_solver
#from selenium import webdriver

#options = webdriver.ChromeOptions()
#options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
#driver = webdriver.Chrome(options=options)
#driver.get("https://accounts.hcaptcha.com/demo") # open any url with hCaptcha

##create Captcha_Solver object and solve hCaptcha
#captcha_solver = hcaptcha_solver.Captcha_Solver(verbose=True)
#captcha_solver.is_captcha_present(driver) # returns True
#captcha_solver.solve_captcha(driver) # solves the hCaptcha

#######################################################################################

        try:

            
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.SUCCESS_HCAPTCHA = int(stat_hv2v3.SUCCESS_HCAPTCHA) + 1

            return f'ERROR_HCAPTCHA_NOT_IMPLEMENTED_YET'
        except Exception as e:
            if not page.is_closed():
                await page.close()
            await browser.close()

            stat_hv2v3.ERROR_HCAPTCHA_EXCEPTION = int(stat_hv2v3.ERROR_HCAPTCHA_EXCEPTION) + 1

            return f'ERROR_HCAPTCHA_EXCEPTION={e}'

############################################################################
# Class Aborting Threads
############################################################################

class abort_thread_v2a(threading.Thread):

    def __init__(self, page_url: str, ran_id: str, loop, stat_hv2v3: c_stat_hv2v3):
        threading.Thread.__init__(self)
        self.page_url = page_url
        self.ran_id = ran_id
        self.loop = loop
        self.stat_hv2v3 = stat_hv2v3
        self.is_stop_thread = False
        self.tempo = 0
    
    def run(self):
        while ((not self.is_stop_thread) and (timeout_in_seconds_aborting_thread_v2a > self.tempo)):
            sleep(1)
            self.tempo = self.tempo + 1
        
        if not self.is_stop_thread:
            if os.path.exists('./captcha/' + self.ran_id + '.txt'):
                self.stat_hv2v3.ABORT_TIMEOUT_RECAPTCHAV2_AUDIO = int(self.stat_hv2v3.ABORT_TIMEOUT_RECAPTCHAV2_AUDIO) + 1
				
                print_sync(f'ABORT TIMEOUT SOLVING RECAPTCHA v2 (AUDIO)',f'URL={self.page_url}',f'ID={self.ran_id}','')

                if is_logging:
                    log_sync_v2('ABORT TIMEOUT SOLVING RECAPTCHA v2 (AUDIO)',f'URL={self.page_url}',f'ID={self.ran_id}','')

                os.remove('./captcha/' + self.ran_id + '.txt')
                self.loop.stop()

    def resetTempo(self):
        self.tempo = 0

    def stop_thread(self):
        self.is_stop_thread = True
				
class abort_thread_v2ic(threading.Thread):

    def __init__(self, page_url: str, ran_id: str, loop, stat_hv2v3: c_stat_hv2v3):
        threading.Thread.__init__(self) 
        self.page_url = page_url
        self.ran_id = ran_id
        self.loop = loop
        self.stat_hv2v3 = stat_hv2v3
        self.is_stop_thread = False
        self.tempo = 0
    
    def run(self):
        while ((not self.is_stop_thread) and (timeout_in_seconds_aborting_thread_v2ic > self.tempo)):
            sleep(1)
            self.tempo = self.tempo + 1

        if not self.is_stop_thread:
            if os.path.exists('./captcha/' + self.ran_id + '.txt'):
                self.stat_hv2v3.ABORT_TIMEOUT_RECAPTCHAV2_IMAGE_CHALLENGE = int(self.stat_hv2v3.ABORT_TIMEOUT_RECAPTCHAV2_IMAGE_CHALLENGE) + 1

                print_sync(f'ABORT TIMEOUT SOLVING RECAPTCHA v2 (IMAGE CHALLENGE)',f'URL={self.page_url}',f'ID={self.ran_id}','')

                if is_logging:
                    log_sync_v2('ABORT TIMEOUT SOLVING RECAPTCHA v2 (IMAGE CHALLENGE)',f'URL={self.page_url}',f'ID={self.ran_id}','')

                os.remove('./captcha/' + self.ran_id + '.txt')
                self.loop.stop()

    def resetTempo(self):
        self.tempo = 0

    def stop_thread(self):
        self.is_stop_thread = True

class abort_thread_v3(threading.Thread):

    def __init__(self, page_url: str, ran_id: str, loop, stat_hv2v3: c_stat_hv2v3):
        threading.Thread.__init__(self) 
        self.page_url = page_url
        self.ran_id = ran_id
        self.loop = loop
        self.stat_hv2v3 = stat_hv2v3
        self.is_stop_thread = False
        self.tempo = 0
    
    def run(self):
        while ((not self.is_stop_thread) and (timeout_in_seconds_aborting_thread_v3 > self.tempo)):
            sleep(1)
            self.tempo = self.tempo + 1

        if not self.is_stop_thread:
            if os.path.exists('./captcha/' + self.ran_id + '.txt'):
                self.stat_hv2v3.ABORT_TIMEOUT_RECAPTCHAV3 = int(self.stat_hv2v3.ABORT_TIMEOUT_RECAPTCHAV3) + 1
				
                print_sync(f'ABORT TIMEOUT SOLVING RECAPTCHA v3',f'URL={self.page_url}',f'ID={self.ran_id}','')

                if is_logging:
                    log_sync_v3('ABORT TIMEOUT SOLVING RECAPTCHA v3',f'URL={self.page_url}',f'ID={self.ran_id}','')

                os.remove('./captcha/' + self.ran_id + '.txt')
                self.loop.stop()

    def resetTempo(self):
        self.tempo = 0

    def stop_thread(self):
        self.is_stop_thread = True

class abort_thread_h(threading.Thread):

    def __init__(self, page_url: str, ran_id: str, loop, stat_hv2v3: c_stat_hv2v3):
        threading.Thread.__init__(self) 
        self.page_url = page_url
        self.ran_id = ran_id
        self.loop = loop
        self.stat_hv2v3 = stat_hv2v3
        self.is_stop_thread = False
        self.tempo = 0
    
    def run(self):
        while ((not self.is_stop_thread) and (timeout_in_seconds_aborting_thread_h > self.tempo)):
            sleep(1)
            self.tempo = self.tempo + 1

        if not self.is_stop_thread:
            if os.path.exists('./captcha/' + self.ran_id + '.txt'):
                self.stat_hv2v3.ABORT_TIMEOUT_HCAPTCHA = int(self.stat_hv2v3.ABORT_TIMEOUT_HCAPTCHA) + 1

                print_sync(f'ABORT TIMEOUT SOLVING HCAPTCHA',f'URL={self.page_url}',f'ID={self.ran_id}','')

                if is_logging:
                    log_sync_h('ABORT TIMEOUT SOLVING HCAPTCHA',f'URL={self.page_url}',f'ID={self.ran_id}','')

                os.remove('./captcha/' + self.ran_id + '.txt')
                self.loop.stop()

    def resetTempo(self):
        self.tempo = 0

    def stop_thread(self):
        self.is_stop_thread = True

############################################################################
# Background Async loop
############################################################################

def background_captchav2_audio_solve(page_url: str, ran_id: str) -> None:

    loop = asyncio.new_event_loop()

    stat_hv2v3 = c_stat_hv2v3()

    try:
        abort_thread = abort_thread_v2a(page_url, ran_id, loop, stat_hv2v3)
        abort_thread.start()

        result = loop.run_until_complete(solve_captchav2_audio(page_url, ran_id, abort_thread, stat_hv2v3))
 
        print_sync(f'RESULT SOLVING RECAPTCHA v2 (AUDIO)',f'URL={page_url}',f'ID={ran_id}',f'RESULT={result}')
        if is_logging:
            log_sync_v2('RESULT SOLVING RECAPTCHA v2 (AUDIO)',f'URL={page_url}',f'ID={ran_id}',f'RESULT={result}')

        if os.path.exists('./captcha/' + ran_id + '.txt'):
            with open('./captcha/' + ran_id + '.txt', 'w') as file:
                file.write(result)
                file.close()

    except Exception as e:
        stat_hv2v3.EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_AUDIO = int(stat_hv2v3.EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_AUDIO) + 1
		
        print_sync(f'EXCEPTION LOOP SOLVING RECAPTCHA v2 (AUDIO)',f'URL={page_url}',f'ID={ran_id}',f'EXCEPTION={e}')

        if is_logging:
            log_sync_v2('EXCEPTION LOOP SOLVING RECAPTCHA v2 (AUDIO)',f'URL={page_url}',f'ID={ran_id}',f'EXCEPTION={e}')

        if os.path.exists('./captcha/' + ran_id + '.txt'):
            with open('./captcha/' + ran_id + '.txt', 'w') as file:
                file.write(f'ERROR_RECAPTCHAV2_EXCEPTION={e}\n')
                file.close()

    finally:
        abort_thread.stop_thread()
		
        if not loop.is_closed():
            loop.close()

        if is_providing_stat_v2a:
            q_stat.put(stat_hv2v3)

            stat_thread = stat_queue_thread()
            stat_thread.start()

def background_captchav2_image_challenge_solve(page_url: str, ran_id: str, my_cap_solver_api_key: str) -> None:

    loop = asyncio.new_event_loop()

    stat_hv2v3 = c_stat_hv2v3()

    try:
        abort_thread = abort_thread_v2ic(page_url, ran_id, loop, stat_hv2v3)
        abort_thread.start()

        result = loop.run_until_complete(solve_captchav2_image_challenge(page_url, ran_id, my_cap_solver_api_key, abort_thread, stat_hv2v3))
		
        print_sync(f'RESULT SOLVING RECAPTCHA v2 (IMAGE CHALLENGE)',f'URL={page_url}',f'ID={ran_id}',f'RESULT={result}')

        if is_logging:
            log_sync_v2('RESULT SOLVING RECAPTCHA v2 (IMAGE CHALLENGE)',f'URL={page_url}',f'ID={ran_id}',f'RESULT={result}')

        if os.path.exists('./captcha/' + ran_id + '.txt'):
            with open('./captcha/' + ran_id + '.txt', 'w') as file:
                file.write(result)
                file.close()

    except Exception as e:
        stat_hv2v3.EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_IMAGE_CHALLENGE = int(stat_hv2v3.EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_IMAGE_CHALLENGE) + 1

        print_sync(f'EXCEPTION LOOP SOLVING RECAPTCHA v2 (IMAGE CHALLENGE)',f'URL={page_url}',f'ID={ran_id}',f'EXCEPTION={e}')

        if is_logging:
            log_sync_v2('EXCEPTION LOOP SOLVING RECAPTCHA v2 (IMAGE CHALLENGE)',f'URL={page_url}',f'ID={ran_id}',f'EXCEPTION={e}')

        if os.path.exists('./captcha/' + ran_id + '.txt'):
            with open('./captcha/' + ran_id + '.txt', 'w') as file:
                file.write(f'ERROR_RECAPTCHAV2_EXCEPTION={e}\n')
                file.close()

    finally:
        abort_thread.stop_thread()

        if not loop.is_closed():
            loop.close()

        if is_providing_stat_v2ic:
            q_stat.put(stat_hv2v3)

            stat_thread = stat_queue_thread()
            stat_thread.start()

def background_captchav3_solve(page_url: str, ran_id: str) -> None:

    loop = asyncio.new_event_loop()

    stat_hv2v3 = c_stat_hv2v3()

    try:
        abort_thread = abort_thread_v3(page_url, ran_id, loop, stat_hv2v3)
        abort_thread.start()

        result = loop.run_until_complete(solve_captchav3(page_url, ran_id, abort_thread, stat_hv2v3))
		
        print_sync(f'RESULT SOLVING RECAPTCHA v3',f'URL={page_url}',f'ID={ran_id}',f'RESULT={result}')

        if is_logging:
            log_sync_v3('RESULT SOLVING RECAPTCHA v3',f'URL={page_url}',f'ID={ran_id}',f'RESULT={result}')
                        
        if os.path.exists('./captcha/' + ran_id + '.txt'):
            with open('./captcha/' + ran_id + '.txt', 'w') as file:
                file.write(result)
                file.close()

    except Exception as e:
        stat_hv2v3.EXCEPTION_LOOP_SOLVING_RECAPTCHAV3 = int(stat_hv2v3.EXCEPTION_LOOP_SOLVING_RECAPTCHAV3) + 1

        print_sync(f'EXCEPTION LOOP SOLVING RECAPTCHA v3',f'URL={page_url}',f'ID={ran_id}',f'EXCEPTION={e}')

        if is_logging:
            log_sync_v3('EXCEPTION LOOP SOLVING RECAPTCHA v3',f'URL={page_url}',f'ID={ran_id}',f'EXCEPTION={e}')

        if os.path.exists('./captcha/' + ran_id + '.txt'):
            with open('./captcha/' + ran_id + '.txt', 'w') as file:
                file.write(f'ERROR_RECAPTCHAV3_EXCEPTION={e}\n')
                file.close()

    finally:
        abort_thread.stop_thread()

        if not loop.is_closed():
            loop.close()

        if is_providing_stat_v3:
            q_stat.put(stat_hv2v3)

            stat_thread = stat_queue_thread()
            stat_thread.start()

def background_hcaptcha_solve(page_url: str, ran_id: str) -> None:

    loop = asyncio.new_event_loop()

    stat_hv2v3 = c_stat_hv2v3()

    try:
        abort_thread = abort_thread_h(page_url, ran_id, loop, stat_hv2v3)
        abort_thread.start()
		
        result = loop.run_until_complete(solve_hcaptcha(page_url, ran_id, abort_thread, stat_hv2v3))
		
        print_sync(f'RESULT SOLVING HCAPTCHA',f'URL={page_url}',f'ID={ran_id}',f'RESULT={result}')

        if is_logging:
            log_sync_h('RESULT SOLVING HCAPTCHA',f'URL={page_url}',f'ID={ran_id}',f'RESULT={result}')
                        
        if os.path.exists('./captcha/' + ran_id + '.txt'):
            with open('./captcha/' + ran_id + '.txt', 'w') as file:
                file.write(result)
                file.close()

    except Exception as e:
        stat_hv2v3.EXCEPTION_LOOP_SOLVING_HCAPTCHA = int(stat_hv2v3.EXCEPTION_LOOP_SOLVING_HCAPTCHA) + 1

        print_sync(f'EXCEPTION LOOP SOLVING HCAPTCHA',f'URL={page_url}',f'ID={ran_id}',f'EXCEPTION={e}')

        if is_logging:
            log_sync_h('EXCEPTION LOOP SOLVING HCAPTCHA',f'URL={page_url}',f'ID={ran_id}',f'EXCEPTION={e}')

        if os.path.exists('./captcha/' + ran_id + '.txt'):
            with open('./captcha/' + ran_id + '.txt', 'w') as file:
                file.write(f'ERROR_HCAPTCHA_EXCEPTION={e}\n')
                file.close()

    finally:
        abort_thread.stop_thread()

        if not loop.is_closed():
            loop.close()

        if is_providing_stat_h:
            q_stat.put(stat_hv2v3)

            stat_thread = stat_queue_thread()
            stat_thread.start()
			
############################################################################
# in.app endpoint to receive captcha parameters
############################################################################

@app.post("/in.php")
async def captcha_solver(request: Request):
    form = await request.form()
    page_url = form.get("pageurl")
    version = form.get("version")
    my_cap_solver_api_key = form.get("key")

    ran_id = str(uuid4())
	
    loop = asyncio.get_running_loop()

    if version == 'h':
        with open('./captcha/' + ran_id + '.txt', 'w') as file:
            file.write('CAPCHA_NOT_READY_HCAPTCHA')
            file.close()
        loop.run_in_executor(executor, background_hcaptcha_solve, page_url, ran_id)

    elif version == 'v3':
        with open('./captcha/' + ran_id + '.txt', 'w') as file:
            file.write('CAPCHA_NOT_READY_RECAPTCHA_V3')
            file.close()
        loop.run_in_executor(executor, background_captchav3_solve, page_url, ran_id)

    elif version == 'v2a':
        with open('./captcha/' + ran_id + '.txt', 'w') as file:
            file.write('CAPCHA_NOT_READY_RECAPTCHA_V2_AUDIO')
            file.close()
        loop.run_in_executor(executor, background_captchav2_audio_solve, page_url, ran_id)

    elif version == 'v2ic':
        with open('./captcha/' + ran_id + '.txt', 'w') as file:
            file.write('CAPCHA_NOT_READY_RECAPTCHA_V2_IMAGE_CHALLENGE')
            file.close()
        loop.run_in_executor(executor, background_captchav2_image_challenge_solve, page_url, ran_id, my_cap_solver_api_key)

    return PlainTextResponse(f'OK|{ran_id}')

############################################################################
# res.app endpoint to respond with captcha status and SOLVING
############################################################################

@app.get("/res.php")
async def get_response_captcha_solver(request: Request):
    action = request.query_params.get("action")
    cap_id = request.query_params.get("id")

    if action == 'getbalance':
        return 100
    elif action == 'get':
        if os.path.exists('./captcha/' + cap_id + '.txt'):
            file = open('./captcha/' + cap_id + '.txt', 'r')
            line = file.readline()
            file.close()

            if line.startswith('CAPCHA_NOT_READY'):
                return PlainTextResponse('CAPCHA_NOT_READY')
            elif line.startswith('OK'):
                return PlainTextResponse(line)
            elif line.startswith('ERROR_'):
                return PlainTextResponse('ERROR_RECAPTCHA_UNSOLVABLE')
        else:
            return PlainTextResponse('ERROR_RECAPTCHA_UNSOLVABLE')
    elif action == 'reportgood':
        return PlainTextResponse('OK_REPORT_RECORDED')		

############################################################################
# Clean files
############################################################################

def clean_files() -> None:

    for captcha_file_name in os.listdir('./captcha'):
        os.remove('./captcha/' + captcha_file_name)

    if os.path.exists(filename_log_h):
        os.remove(filename_log_h)
    if os.path.exists(filename_log_v2):
        os.remove(filename_log_v2)
    if os.path.exists(filename_log_v3):
        os.remove(filename_log_v3)

    if os.path.exists(filename_stat_h):
        os.remove(filename_stat_h)
    if os.path.exists(filename_stat_v2a):
        os.remove(filename_stat_v2a)
    if os.path.exists(filename_stat_v2ic):
        os.remove(filename_stat_v2ic)
    if os.path.exists(filename_stat_v3):
        os.remove(filename_stat_v3)

    if os.path.exists(filename_stat_temp):
        os.remove(filename_stat_temp)

    if os.path.exists(filename_worked_proxy_h):
        os.remove(filename_worked_proxy_h)
    if os.path.exists(filename_worked_proxy_v2):
        os.remove(filename_worked_proxy_v2)
    if os.path.exists(filename_worked_proxy_v3):
        os.remove(filename_worked_proxy_v3)

    if os.path.exists(filename_failed_proxy_h):
        os.remove(filename_failed_proxy_h)
    if os.path.exists(filename_failed_proxy_v2):
        os.remove(filename_failed_proxy_v2)
    if os.path.exists(filename_failed_proxy_v3):
        os.remove(filename_failed_proxy_v3)

############################################################################
# Initialize mtime filename_proxy_v2 when folder empty
############################################################################

async def initialize_mtime_filename_proxy_v2() -> None:
	
	count_files = 0

	for file_name in os.listdir('./captcha'):
		if file_name.endswith('.txt'):
			count_files = count_files + 1

	if count_files == 0:
		if os.path.exists(filename_proxy_v2):
			if os.path.getsize(filename_proxy_v2) > 0:
				file = open(filename_proxy_v2, 'r+')
				lines = file.readlines()
				file.seek(0)
				file.truncate()
				for line in lines:
					file.write(line)
				file.close()
                    
############################################################################
# Initialize mtime filename_proxy_v3 when folder empty
############################################################################

async def initialize_mtime_filename_proxy_v3() -> None:
	
	count_files = 0

	for file_name in os.listdir('./captcha'):
		if file_name.endswith('.txt'):
			count_files = count_files + 1

	if count_files == 0:
		if os.path.exists(filename_proxy_v3):
			if os.path.getsize(filename_proxy_v3) > 0:
				file = open(filename_proxy_v3, 'r+')
				lines = file.readlines()
				file.seek(0)
				file.truncate()
				for line in lines:
					file.write(line)
				file.close()

############################################################################
# Initialize mtime filename_proxy_h when folder empty
############################################################################

async def initialize_mtime_filename_proxy_h() -> None:
	
	count_files = 0

	for file_name in os.listdir('./captcha'):
		if file_name.endswith('.txt'):
			count_files = count_files + 1

	if count_files == 0:
		if os.path.exists(filename_proxy_h):
			if os.path.getsize(filename_proxy_h) > 0:
				file = open(filename_proxy_h, 'r+')
				lines = file.readlines()
				file.seek(0)
				file.truncate()
				for line in lines:
					file.write(line)
				file.close()

############################################################################
# delete_rotating_proxy_v2
############################################################################

async def delete_rotating_proxy_v2(a_proxy_to_delete : str) -> None:

    if os.path.exists(filename_rotating_proxy_v2):
        if os.path.getsize(filename_rotating_proxy_v2) > 0:
            file = open(filename_rotating_proxy_v2, 'r+')
            lines = file.readlines()

            file.seek(0)
            file.truncate()

            line_number = 0
            for line in lines:
                if a_proxy_to_delete not in line:
                    file.write(line)
                    line_number = line_number + 1

            file.close()
			
            await print_async('ROTATING PROXY RECAPTCHA v2 DELETED',f'PROXY={a_proxy_to_delete}',f'AVAILABLE={line_number}','')

            if is_logging:
                await log_async_v2('ROTATING PROXY RECAPTCHA v2 DELETED',f'PROXY={a_proxy_to_delete}',f'AVAILABLE={line_number}','')

############################################################################
# delete_rotating_proxy_v3
############################################################################

async def delete_rotating_proxy_v3(a_proxy_to_delete : str) -> None:

    if os.path.exists(filename_rotating_proxy_v3):
        if os.path.getsize(filename_rotating_proxy_v3) > 0:
            file = open(filename_rotating_proxy_v3, 'r+')
            lines = file.readlines()

            file.seek(0)
            file.truncate()

            line_number = 0
            for line in lines:
                if a_proxy_to_delete not in line:
                    file.write(line)
                    line_number = line_number + 1

            file.close()
			
            await print_async('ROTATING PROXY RECAPTCHA v3 DELETED',f'PROXY={a_proxy_to_delete}',f'AVAILABLE={line_number}','')

            if is_logging:
                await log_async_v3('ROTATING PROXY RECAPTCHA v3 DELETED',f'PROXY={a_proxy_to_delete}',f'AVAILABLE={line_number}','')


############################################################################
# delete_rotating_proxy_h
############################################################################

async def delete_rotating_proxy_h(a_proxy_to_delete : str) -> None:

    if os.path.exists(filename_rotating_proxy_h):
        if os.path.getsize(filename_rotating_proxy_h) > 0:
            file = open(filename_rotating_proxy_h, 'r+')
            lines = file.readlines()

            file.seek(0)
            file.truncate()

            line_number = 0
            for line in lines:
                if a_proxy_to_delete not in line:
                    file.write(line)
                    line_number = line_number + 1

            file.close()
			
            await print_async('ROTATING PROXY HCAPTCHA DELETED',f'PROXY={a_proxy_to_delete}',f'AVAILABLE={line_number}','')

            if is_logging:
                await log_async_h('ROTATING PROXY HCAPTCHA DELETED',f'PROXY={a_proxy_to_delete}',f'AVAILABLE={line_number}','')

############################################################################
# get_proxy_v2
# HOST:PORT:USERNAME:PASSWORD
# HOST:PORT
############################################################################

async def get_proxy_v2(force_new_random_proxy : bool) -> str:

    if os.path.exists(filename_rotating_proxy_v2):
        if os.path.getsize(filename_rotating_proxy_v2) > 0:
            file = open(filename_rotating_proxy_v2, 'r+')
            lines = file.readlines()
            
            if len(lines) == 0:
                file.close()
                return 'NO_PROXY'	

            if len(lines) == 1:
                file.close()
	
                a_line = lines[0].strip()

                await print_async(f'NEW ROTATING PROXY RECAPTCHA v2 - PROXY={a_line}','','','')

                if is_logging:
                    await log_async_v2(f'NEW ROTATING PROXY RECAPTCHA v2 - PROXY={a_line}','','','')

                return a_line	

            first_line = lines[0]
            lines = lines[1:]

            file.seek(0)
            file.truncate()
						
            for line in lines:
                if not line.isspace():
                    file.write(line)

            file.write(first_line)
            file.close()

            a_line = first_line.strip()
			
            await print_async(f'NEW ROTATING PROXY RECAPTCHA v2 - PROXY={a_line}','','','')

            if is_logging:
                await log_async_v3(f'NEW ROTATING PROXY RECAPTCHA v2 - PROXY={a_line}','','','')

            return f'{a_line}'
        else:
            return 'NO_PROXY'

    threshold_time_get_proxy_v2 = datetime.now() - timedelta(seconds=interval_in_seconds_new_random_proxy_v2)

    if os.path.exists(filename_proxy_v2):
        if (datetime.fromtimestamp(os.path.getmtime(filename_proxy_v2)) < threshold_time_get_proxy_v2):
            await initialize_mtime_filename_proxy_v2()

    if os.path.exists(filename_proxy_v2):
        if os.path.getsize(filename_proxy_v2) > 0:
            try:					
                if ((datetime.fromtimestamp(os.path.getmtime(filename_proxy_v2)) < threshold_time_get_proxy_v2) or force_new_random_proxy):
                    #proxy is too old or forced new
					
					#get random proxy and put it at first
                    file = open(filename_proxy_v2, 'r+')
                    lines = file.readlines()
                    					
                    if len(lines) == 1:
                        file.seek(0)
                        file.truncate()
                        file.close()
                
                        await print_async(f'WARNING : PROXY FILE RECAPTCHA v2 IS EMPTY','','','')
                        
                        if is_logging:
                            await log_async_v2('WARNING : PROXY FILE RECAPTCHA v2 IS EMPTY','','','')

                        return'NO_PROXY'

                    a_random_line = 'NO_PROXY'
                    a_random_line_number = 0

                    if len(lines) > 1:
                        a_random_line_number = random.randint(2, len(lines))
                    
                    #get proxy from random line
                    line_number = 1
                    for line in lines:
                        if line_number == a_random_line_number:
                            a_random_line = line.strip()
                        line_number = line_number + 1
                    
                    await print_async(f'NEW RANDOM PROXY RECAPTCHA v2',f'PROXY={a_random_line}',f'AVAILABLE={line_number-2}','')
 
                    if is_logging:
                        await log_async_v2('NEW RANDOM PROXY RECAPTCHA v2',f'PROXY={a_random_line}',f'AVAILABLE={line_number-2}','')

                    file.seek(0)
                    file.truncate()

                    #rewrite file (delete first then move to first)
                    line_number = 1
                    for line in lines:
                        if line_number == 1:
                            file.write(a_random_line + '\n')
                        else:
                            if line_number != a_random_line_number:
                                file.write(line)
                        line_number = line_number + 1

                    file.close()
                    return a_random_line
                else:
                    #get first proxy if not too old and not forced new
                    file = open(filename_proxy_v2, 'r')
                    a_random_proxy = file.readline().strip()
                    file.close()

                    return a_random_proxy
					
            except Exception as e:
                file.close()
                await print_async('EXCEPTION IN PROXY FILE RECAPTCHA v2',f'EXCEPTION={e}','','')

                if is_logging:
                    await log_async_v2('EXCEPTION IN PROXY FILE RECAPTCHA v2',f'EXCEPTON={e}','','')

        else:
            await print_async(f'WARNING : PROXY FILE RECAPTCHA v2 IS EMPTY','','','')

            if is_logging:
                await log_async_v2('WARNING : PROXY FILE RECAPTCHA v2 IS EMPTY','','','')

    return 'NO_PROXY'

############################################################################
# get_proxy_v3
# HOST:PORT:USERNAME:PASSWORD
# HOST:PORT
############################################################################

async def get_proxy_v3(force_new_random_proxy : bool) -> str:

    if os.path.exists(filename_rotating_proxy_v3):
        if os.path.getsize(filename_rotating_proxy_v3) > 0:
            file = open(filename_rotating_proxy_v3, 'r+')
            lines = file.readlines()
            
            if len(lines) == 0:
                file.close()
                return 'NO_PROXY'	

            if len(lines) == 1:
                file.close()
	
                a_line = lines[0].strip()

                await print_async(f'NEW ROTATING PROXY RECAPTCHA v3 - PROXY={a_line}','','','')

                if is_logging:
                    await log_async_v3(f'NEW ROTATING PROXY RECAPTCHA v3 - PROXY={a_line}','','','')

                return a_line	

            first_line = lines[0]
            lines = lines[1:]

            file.seek(0)
            file.truncate()
						
            for line in lines:
                if not line.isspace():
                    file.write(line)

            file.write(first_line)
            file.close()

            a_line = first_line.strip()
			
            await print_async(f'NEW ROTATING PROXY RECAPTCHA v3 - PROXY={a_line}','','','')

            if is_logging:
                await log_async_v3(f'NEW ROTATING PROXY RECAPTCHA v3 - PROXY={a_line}','','','')

            return f'{a_line}'
        else:
            return 'NO_PROXY'

    threshold_time_get_proxy_v3 = datetime.now() - timedelta(seconds=interval_in_seconds_new_random_proxy_v3)

    if os.path.exists(filename_proxy_v3):
        if (datetime.fromtimestamp(os.path.getmtime(filename_proxy_v3)) < threshold_time_get_proxy_v3):
            await initialize_mtime_filename_proxy_v3()

    if os.path.exists(filename_proxy_v3):
        if os.path.getsize(filename_proxy_v3) > 0:
            try:					
                if ((datetime.fromtimestamp(os.path.getmtime(filename_proxy_v3)) < threshold_time_get_proxy_v3) or force_new_random_proxy):
                    #proxy is too old or forced new
					
					#get random proxy and put it at first
                    file = open(filename_proxy_v3, 'r+')
                    lines = file.readlines()
                    					
                    if len(lines) == 1:
                        file.seek(0)
                        file.truncate()
                        file.close()
                
                        await print_async(f'WARNING : PROXY FILE RECAPTCHA v3 IS EMPTY','','','')
                        
                        if is_logging:
                            await log_async_v3('WARNING : PROXY FILE RECAPTCHA v3 IS EMPTY','','','')

                        return'NO_PROXY'

                    a_random_line = 'NO_PROXY'
                    a_random_line_number = 0

                    if len(lines) > 1:
                        a_random_line_number = random.randint(2, len(lines))
                    
                    #get proxy from random line
                    line_number = 1
                    for line in lines:
                        if line_number == a_random_line_number:
                            a_random_line = line.strip()
                        line_number = line_number + 1
                    
                    await print_async(f'NEW RANDOM PROXY RECAPTCHA v3',f'PROXY={a_random_line}',f'AVAILABLE={line_number-2}','')

                    if is_logging:
                        await log_async_v3('NEW RANDOM PROXY RECAPTCHA v3',f'PROXY={a_random_line}',f'AVAILABLE={line_number-2}','')

                    file.seek(0)
                    file.truncate()

                    #rewrite file (delete first then move to first)
                    line_number = 1
                    for line in lines:
                        if line_number == 1:
                            file.write(a_random_line + '\n')
                        else:
                            if line_number != a_random_line_number:
                                file.write(line)
                        line_number = line_number + 1

                    file.close()
                    return a_random_line
                else:
                    #get first proxy if not too old and not forced new
                    file = open(filename_proxy_v3, 'r')
                    a_random_proxy = file.readline().strip()
                    file.close()
                    return a_random_proxy
					
            except Exception as e:
                file.close()
                await print_async('EXCEPTION IN PROXY FILE RECAPTCHA v3',f'EXCEPTION={e}','','')

                if is_logging:
                    await log_async_v3('EXCEPTION IN PROXY FILE RECAPTCHA v3',f'EXCEPTION={e}','','')

        else:
            await print_async(f'WARNING : PROXY FILE RECAPTCHA v3 IS EMPTY','','','')

            if is_logging:
                await log_async_v3('WARNING : PROXY FILE RECAPTCHA v3 IS EMPTY','','','')

    return 'NO_PROXY'


############################################################################
# get_proxy_h
# HOST:PORT:USERNAME:PASSWORD
# HOST:PORT
############################################################################

async def get_proxy_h(force_new_random_proxy : bool) -> str:

    if os.path.exists(filename_rotating_proxy_h):
        if os.path.getsize(filename_rotating_proxy_h) > 0:
            file = open(filename_rotating_proxy_h, 'r+')
            lines = file.readlines()
            
            if len(lines) == 0:
                file.close()
                return 'NO_PROXY'	

            if len(lines) == 1:
                file.close()
	
                a_line = lines[0].strip()

                await print_async(f'NEW ROTATING PROXY HCAPTCHA - PROXY={a_line}','','','')

                if is_logging:
                    await log_async_v3(f'NEW ROTATING PROXY HCAPTCHA - PROXY={a_line}','','','')

                return a_line	

            first_line = lines[0]
            lines = lines[1:]

            file.seek(0)
            file.truncate()
						
            for line in lines:
                if not line.isspace():
                    file.write(line)

            file.write(first_line)
            file.close()

            a_line = first_line.strip()
								
            await print_async('NEW ROTATING PROXY HCAPTCHA',f'PROXY={a_line}','','')

            if is_logging:
                await log_async_h('NEW ROTATING PROXY HCAPTCHA',f'PROXY={a_line}','','')

            return f'{a_line}'
        else:
            return 'NO_PROXY'
		
    threshold_time_get_proxy_h = datetime.now() - timedelta(seconds=interval_in_seconds_new_random_proxy_h)

    if os.path.exists(filename_proxy_h):
        if (datetime.fromtimestamp(os.path.getmtime(filename_proxy_h)) < threshold_time_get_proxy_h):
            await initialize_mtime_filename_proxy_h()

    if os.path.exists(filename_proxy_h):
        if os.path.getsize(filename_proxy_h) > 0:
            try:					
                if ((datetime.fromtimestamp(os.path.getmtime(filename_proxy_h)) < threshold_time_get_proxy_h) or force_new_random_proxy):
                    #proxy is too old or forced new
					
					#get random proxy and put it at first
                    file = open(filename_proxy_h, 'r+')
                    lines = file.readlines()
                    					
                    if len(lines) == 1:
                        file.seek(0)
                        file.truncate()
                        file.close()
                
                        await print_async(f'WARNING : PROXY FILE HCAPTCHA IS EMPTY','','','')
                         
                        if is_logging:
                            await log_async_h('WARNING : PROXY FILE HCAPTCHA IS EMPTY','','','')

                        return'NO_PROXY'

                    a_random_line = 'NO_PROXY'
                    a_random_line_number = 0

                    if len(lines) > 1:
                        a_random_line_number = random.randint(2, len(lines))
                    
                    #get proxy from random line
                    line_number = 1
                    for line in lines:
                        if line_number == a_random_line_number:
                            a_random_line = line.strip()
                        line_number = line_number + 1
                    
                    await print_async(f'NEW RANDOM PROXY HCAPTCHA',f'PROXY={a_random_line}',f'AVAILABLE={line_number-2}','')

                    if is_logging:
                        await log_async_h('NEW RANDOM PROXY HCAPTCHA',f'PROXY={a_random_line}',f'AVAILABLE={line_number-2}','')

                    file.seek(0)
                    file.truncate()

                    #rewrite file (delete first then move to first)
                    line_number = 1
                    for line in lines:
                        if line_number == 1:
                            file.write(a_random_line + '\n')
                        else:
                            if line_number != a_random_line_number:
                                file.write(line)
                        line_number = line_number + 1

                    file.close()
                    return a_random_line
                else:
                    #get first proxy if not too old and not forced new
                    file = open(filename_proxy_h, 'r')
                    a_random_proxy = file.readline().strip()
                    file.close()
                    return a_random_proxy
					
            except Exception as e:
                file.close()
                await print_async('EXCEPTION IN PROXY FILE HCAPTCHA',f'EXCEPTION={e}','','')

                if is_logging:
                    await log_async_h('EXCEPTION IN PROXY FILE HCAPTCHA',f'EXCEPTION={e}','','')

        else:
            await print_async(f'WARNING : PROXY FILE HCAPTCHA IS EMPTY','','','')

            if is_logging:
                await log_async_h('WARNING : PROXY FILE HCAPTCHA IS EMPTY','','','')

    return 'NO_PROXY'
	
############################################################################
# log_async_v2
############################################################################

async def log_async_v2(line1 : str, line2 : str, line3 : str, line4 : str) -> None:
    with open(filename_log_v2, 'a') as file:
        if line1 != '':
            file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line1 + '\n')
        if line2 != '':
            file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line2 + '\n')
        if line3 != '':
            file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line3 + '\n')
        if line4 != '':
            file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line4 + '\n')
        file.write('######################################################################################################################\n')
        file.close()

############################################################################
# log_async_v3
############################################################################

async def log_async_v3(line1 : str, line2 : str, line3 : str, line4 : str) -> None:
    with open(filename_log_v3, 'a') as file:
        if line1 != '':
            file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line1 + '\n')
        if line2 != '':
            file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line2 + '\n')
        if line3 != '':
            file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line3 + '\n')
        if line4 != '':
            file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line4 + '\n')
        file.write('######################################################################################################################\n')
        file.close()

############################################################################
# log_async_h
############################################################################

async def log_async_h(line1 : str, line2 : str, line3 : str, line4 : str) -> None:
    with open(filename_log_h, 'a') as file:
        if line1 != '':
            file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line1 + '\n')
        if line2 != '':
            file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line2 + '\n')
        if line3 != '':
            file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line3 + '\n')
        if line4 != '':
            file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line4 + '\n')
        file.write('######################################################################################################################\n')
        file.close()
		
############################################################################
# log_sync_v2
############################################################################

def log_sync_v2(line1 : str, line2 : str, line3 : str, line4 : str) -> None:
    loop = asyncio.new_event_loop()
    loop.run_until_complete(log_async_v2(line1, line2, line3, line4))
    loop.close()

############################################################################
# log_sync_v3
############################################################################

def log_sync_v3(line1 : str, line2 : str, line3 : str, line4 : str) -> None:
    loop = asyncio.new_event_loop()
    loop.run_until_complete(log_async_v3(line1, line2, line3, line4))
    loop.close()
		
############################################################################
# log_sync_h
############################################################################

def log_sync_h(line1 : str, line2 : str, line3 : str, line4 : str) -> None:
    loop = asyncio.new_event_loop()
    loop.run_until_complete(log_async_h(line1, line2, line3, line4))
    loop.close()
		
############################################################################
# add_worked_proxy_v2
############################################################################

async def add_worked_proxy_v2(proxy : str) -> None:
    exists_proxy = await exists_worked_proxy_v2(proxy)
    if not exists_proxy:
        with open(filename_worked_proxy_v2, 'a') as file:
            file.write(proxy + '\n')
            file.close()

############################################################################
# add_worked_proxy_v3
############################################################################

async def add_worked_proxy_v3(proxy : str) -> None:
    exists_proxy = await exists_worked_proxy_v3(proxy)
    if not exists_proxy:
        with open(filename_worked_proxy_v3, 'a') as file:
            file.write(proxy + '\n')
            file.close()

############################################################################
# add_worked_proxy_h
############################################################################

async def add_worked_proxy_h(proxy : str) -> None:
    exists_proxy = await exists_worked_proxy_h(proxy)
    if not exists_proxy:
        with open(filename_worked_proxy_h, 'a') as file:
            file.write(proxy + '\n')
            file.close()

############################################################################
# exists_worked_proxy_v2
############################################################################

async def exists_worked_proxy_v2(proxy : str) -> bool:
    is_found = False
    if os.path.exists(filename_worked_proxy_v2):
        with open(filename_worked_proxy_v2, 'r') as file:
            for line in file.readlines():
                if line.strip() == proxy:
                    is_found = True
            file.close()
    return is_found

############################################################################
# exists_worked_proxy_v3
############################################################################

async def exists_worked_proxy_v3(proxy : str) -> bool:
    is_found = False
    if os.path.exists(filename_worked_proxy_v3):
        with open(filename_worked_proxy_v3, 'r') as file:
            for line in file.readlines():
                if line.strip() == proxy:
                    is_found = True
            file.close()
    return is_found

############################################################################
# exists_worked_proxy_h
############################################################################

async def exists_worked_proxy_h(proxy : str) -> bool:
    is_found = False
    if os.path.exists(filename_worked_proxy_h):
        with open(filename_worked_proxy_h, 'r') as file:
            for line in file.readlines():
                if line.strip() == proxy:
                    is_found = True
            file.close()
    return is_found

############################################################################
# add_failed_proxy_v2
############################################################################

async def add_failed_proxy_v2(proxy : str) -> None:
    exists_proxy = await exists_failed_proxy_v2(proxy)
    if not exists_proxy:
        with open(filename_failed_proxy_v2, 'a') as file:
            file.write(proxy + '\n')
            file.close()

############################################################################
# add_failed_proxy_v3
############################################################################

async def add_failed_proxy_v3(proxy : str) -> None:
    exists_proxy = await exists_failed_proxy_v3(proxy)
    if not exists_proxy:
        with open(filename_failed_proxy_v3, 'a') as file:
            file.write(proxy + '\n')
            file.close()

############################################################################
# add_failed_proxy_h
############################################################################

async def add_failed_proxy_h(proxy : str) -> None:
    exists_proxy = await exists_failed_proxy_h(proxy)
    if not exists_proxy:
        with open(filename_failed_proxy_h, 'a') as file:
            file.write(proxy + '\n')
            file.close()

############################################################################
# exists_failed_proxy_v2
############################################################################

async def exists_failed_proxy_v2(proxy : str) -> bool:
    is_found = False
    if os.path.exists(filename_failed_proxy_v2):
        with open(filename_failed_proxy_v2, 'r') as file:
            for line in file.readlines():
                if line.strip() == proxy:
                    is_found = True
            file.close()
    return is_found

############################################################################
# exists_failed_proxy_v3
############################################################################

async def exists_failed_proxy_v3(proxy : str) -> bool:
    is_found = False
    if os.path.exists(filename_failed_proxy_v3):
        with open(filename_failed_proxy_v3, 'r') as file:
            for line in file.readlines():
                if line.strip() == proxy:
                    is_found = True
            file.close()
    return is_found

############################################################################
# exists_worked_proxy_h
############################################################################

async def exists_worked_proxy_h(proxy : str) -> bool:
    is_found = False
    if os.path.exists(filename_worked_proxy_h):
        with open(filename_worked_proxy_h, 'r') as file:
            for line in file.readlines():
                if line.strip() == proxy:
                    is_found = True
            file.close()
    return is_found
	
############################################################################
# print_sync
############################################################################

def print_sync(line1 : str, line2 : str, line3 : str, line4 : str) -> None:
    loop = asyncio.new_event_loop()
    loop.run_until_complete(print_async(line1, line2, line3, line4))
    loop.close()

############################################################################
# print_async
############################################################################

async def print_async(line1 : str, line2 : str, line3 : str, line4 : str) -> None:

    print_async_str = '### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line1 + '\n'
    if line2 != '':
        print_async_str = print_async_str + '### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line2 + '\n'
    if line3 != '':
        print_async_str = print_async_str + '### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line3 + '\n'
    if line4 != '':
        print_async_str = print_async_str + '### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + ' : ' + line4 + '\n'

    print_async_str = print_async_str + '######################################################################################################################'
    print(print_async_str)

############################################################################
# Queue Stats
############################################################################

class stat_queue_thread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while not q_stat.empty():
            stat_hv2v3 = q_stat.get()
            
            RECAPTCHAV2_AUDIO = 0
            TRYS_RECAPTCHAV2_AUDIO = 0
            TRY1_RECAPTCHAV2_AUDIO = 0
            TRY2_RECAPTCHAV2_AUDIO = 0
            TRY3_RECAPTCHAV2_AUDIO = 0
            SUCCESS_RECAPTCHAV2_AUDIO = 0
            ERROR_RECAPTCHAV2_AUDIO_NOT_FOUND = 0
            ERROR_RECAPTCHAV2_AUDIO_RATE_LIMIT = 0
            ERROR_RECAPTCHAV2_AUDIO_SOLVE = 0
            ERROR_RECAPTCHAV2_AUDIO = 0
            ERROR_RECAPTCHAV2_AUDIO_EXCEPTION = 0
            ERROR_CONNECTION_RECAPTCHAV2_AUDIO = 0
            ABORT_TIMEOUT_RECAPTCHAV2_AUDIO = 0
            EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_AUDIO = 0

            RECAPTCHAV2_IMAGE_CHALLENGE = 0
            TRYS_RECAPTCHAV2_IMAGE_CHALLENGE = 0
            TRY1_RECAPTCHAV2_IMAGE_CHALLENGE = 0
            TRY2_RECAPTCHAV2_IMAGE_CHALLENGE = 0
            TRY3_RECAPTCHAV2_IMAGE_CHALLENGE = 0
            SUCCESS_RECAPTCHAV2_IMAGE_CHALLENGE = 0
            ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_CAP_SOLVER = 0
            ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_NOT_FOUND = 0
            ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_RATE_LIMIT = 0
            ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_SOLVE = 0
            ERROR_RECAPTCHAV2_IMAGE_CHALLENGE = 0
            ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_EXCEPTION = 0
            ERROR_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE = 0
            ABORT_TIMEOUT_RECAPTCHAV2_IMAGE_CHALLENGE = 0
            EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_IMAGE_CHALLENGE = 0

            RECAPTCHAV3 = 0
            TRYS_RECAPTCHAV3 = 0
            TRY1_RECAPTCHAV3 = 0
            TRY2_RECAPTCHAV3 = 0
            TRY3_RECAPTCHAV3 = 0
            SUCCESS_RECAPTCHAV3 = 0
            ERROR_RECAPTCHAV3_NOT_FOUND = 0
            ERROR_RECAPTCHAV3_RATE_LIMIT = 0
            ERROR_RECAPTCHAV3_SOLVE = 0
            ERROR_RECAPTCHAV3 = 0
            ERROR_RECAPTCHAV3_EXCEPTION = 0
            ERROR_CONNECTION_RECAPTCHAV3 = 0
            ABORT_TIMEOUT_RECAPTCHAV3 = 0
            EXCEPTION_LOOP_SOLVING_RECAPTCHAV3 = 0

            HCAPTCHA = 0
            TRYS_HCAPTCHA = 0
            TRY1_HCAPTCHA = 0
            TRY2_HCAPTCHA = 0
            TRY3_HCAPTCHA = 0
            SUCCESS_HCAPTCHA = 0
            ERROR_CONNECTION_HCAPTCHA = 0
            ABORT_TIMEOUT_HCAPTCHA = 0
            EXCEPTION_LOOP_SOLVING_HCAPTCHA = 0

            if os.path.exists(filename_stat_temp):
                file = open(filename_stat_temp, 'r')
                lines = file.readlines()

                line_number = 0
                for line in lines:
                    if line_number == 0:
                        RECAPTCHAV2_AUDIO = int(line.strip())
                    if line_number == 1:
                        TRYS_RECAPTCHAV2_AUDIO = int(line.strip())
                    if line_number == 2:
                        TRY1_RECAPTCHAV2_AUDIO = int(line.strip())
                    if line_number == 3:
                        TRY2_RECAPTCHAV2_AUDIO = int(line.strip())
                    if line_number == 4:
                        TRY3_RECAPTCHAV2_AUDIO = int(line.strip())
                    if line_number == 5:
                        SUCCESS_RECAPTCHAV2_AUDIO = int(line.strip())
                    if line_number == 6:
                        ERROR_RECAPTCHAV2_AUDIO_NOT_FOUND = int(line.strip())
                    if line_number == 7:
                        ERROR_RECAPTCHAV2_AUDIO_RATE_LIMIT = int(line.strip())
                    if line_number == 8:
                        ERROR_RECAPTCHAV2_AUDIO_SOLVE = int(line.strip())
                    if line_number == 9:
                        ERROR_RECAPTCHAV2_AUDIO = int(line.strip())
                    if line_number == 10:
                        ERROR_RECAPTCHAV2_AUDIO_EXCEPTION = int(line.strip())
                    if line_number == 11:
                        ERROR_CONNECTION_RECAPTCHAV2_AUDIO = int(line.strip())
                    if line_number == 12:
                        ABORT_TIMEOUT_RECAPTCHAV2_AUDIO = int(line.strip())
                    if line_number == 13:
                        EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_AUDIO = int(line.strip())

                    if line_number == 14:
                        RECAPTCHAV2_IMAGE_CHALLENGE = int(line.strip())
                    if line_number == 15:
                        TRYS_RECAPTCHAV2_IMAGE_CHALLENGE = int(line.strip())
                    if line_number == 16:
                        TRY1_RECAPTCHAV2_IMAGE_CHALLENGE = int(line.strip())
                    if line_number == 17:
                        TRY2_RECAPTCHAV2_IMAGE_CHALLENGE = int(line.strip())
                    if line_number == 18:
                        TRY3_RECAPTCHAV2_IMAGE_CHALLENGE = int(line.strip())
                    if line_number == 19:
                        SUCCESS_RECAPTCHAV2_IMAGE_CHALLENGE = int(line.strip())
                    if line_number == 20:
                        ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_CAP_SOLVER = int(line.strip())
                    if line_number == 21:
                        ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_NOT_FOUND = int(line.strip())
                    if line_number == 22:
                        ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_RATE_LIMIT = int(line.strip())
                    if line_number == 23:
                        ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_SOLVE = int(line.strip())
                    if line_number == 24:
                        ERROR_RECAPTCHAV2_IMAGE_CHALLENGE = int(line.strip())
                    if line_number == 25:
                        ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_EXCEPTION = int(line.strip())
                    if line_number == 26:
                        ERROR_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE = int(line.strip())
                    if line_number == 27:
                        ABORT_TIMEOUT_RECAPTCHAV2_IMAGE_CHALLENGE = int(line.strip())
                    if line_number == 28:
                        EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_IMAGE_CHALLENGE = int(line.strip())

                    if line_number == 29:
                        RECAPTCHAV3 = int(line.strip())
                    if line_number == 30:
                        TRYS_RECAPTCHAV3 = int(line.strip())
                    if line_number == 31:
                        TRY1_RECAPTCHAV3 = int(line.strip())
                    if line_number == 32:
                        TRY2_RECAPTCHAV3 = int(line.strip())
                    if line_number == 33:
                        TRY3_RECAPTCHAV3 = int(line.strip())
                    if line_number == 34:
                        SUCCESS_RECAPTCHAV3 = int(line.strip())
                    if line_number == 35:
                        ERROR_RECAPTCHAV3_NOT_FOUND = int(line.strip())
                    if line_number == 36:
                        ERROR_RECAPTCHAV3_RATE_LIMIT = int(line.strip())
                    if line_number == 37:
                        ERROR_RECAPTCHAV3_SOLVE = int(line.strip())
                    if line_number == 38:
                        ERROR_RECAPTCHAV3 = int(line.strip())
                    if line_number == 39:
                        ERROR_RECAPTCHAV3_EXCEPTION = int(line.strip())
                    if line_number == 40:
                        ERROR_CONNECTION_RECAPTCHAV3 = int(line.strip())
                    if line_number == 41:
                        ABORT_TIMEOUT_RECAPTCHAV3 = int(line.strip())
                    if line_number == 42:
                        EXCEPTION_LOOP_SOLVING_RECAPTCHAV3 = int(line.strip())

                    if line_number == 43:
                        HCAPTCHA = int(line.strip())
                    if line_number == 44:
                        TRYS_HCAPTCHA = int(line.strip())
                    if line_number == 45:
                        TRY1_HCAPTCHA = int(line.strip())
                    if line_number == 46:
                        TRY2_HCAPTCHA = int(line.strip())
                    if line_number == 47:
                        TRY3_HCAPTCHA = int(line.strip())
                    if line_number == 48:
                        SUCCESS_HCAPTCHA = int(line.strip())
                    if line_number == 49:
                        ERROR_CONNECTION_HCAPTCHA = int(line.strip())
                    if line_number == 50:
                        ABORT_TIMEOUT_HCAPTCHA = int(line.strip())
                    if line_number == 51:
                        EXCEPTION_LOOP_SOLVING_HCAPTCHA = int(line.strip())
						
                    line_number = line_number + 1
                                
                file.close()

            RECAPTCHAV2_AUDIO = int(RECAPTCHAV2_AUDIO) + int(stat_hv2v3.RECAPTCHAV2_AUDIO)
            TRYS_RECAPTCHAV2_AUDIO = int(TRYS_RECAPTCHAV2_AUDIO) + int(stat_hv2v3.TRYS_RECAPTCHAV2_AUDIO)
            TRY1_RECAPTCHAV2_AUDIO = int(TRY1_RECAPTCHAV2_AUDIO) + int(stat_hv2v3.TRY1_RECAPTCHAV2_AUDIO)
            TRY2_RECAPTCHAV2_AUDIO = int(TRY2_RECAPTCHAV2_AUDIO) + int(stat_hv2v3.TRY2_RECAPTCHAV2_AUDIO)
            TRY3_RECAPTCHAV2_AUDIO = int(TRY3_RECAPTCHAV2_AUDIO) + int(stat_hv2v3.TRY3_RECAPTCHAV2_AUDIO)
            SUCCESS_RECAPTCHAV2_AUDIO = int(SUCCESS_RECAPTCHAV2_AUDIO) + int(stat_hv2v3.SUCCESS_RECAPTCHAV2_AUDIO)
            ERROR_RECAPTCHAV2_AUDIO_NOT_FOUND = int(ERROR_RECAPTCHAV2_AUDIO_NOT_FOUND) + int(stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO_NOT_FOUND)
            ERROR_RECAPTCHAV2_AUDIO_RATE_LIMIT = int(ERROR_RECAPTCHAV2_AUDIO_RATE_LIMIT) + int(stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO_RATE_LIMIT)
            ERROR_RECAPTCHAV2_AUDIO_SOLVE = int(ERROR_RECAPTCHAV2_AUDIO_SOLVE) + int(stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO_SOLVE)
            ERROR_RECAPTCHAV2_AUDIO = int(ERROR_RECAPTCHAV2_AUDIO) + int(stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO)
            ERROR_RECAPTCHAV2_AUDIO_EXCEPTION = int(ERROR_RECAPTCHAV2_AUDIO_EXCEPTION) + int(stat_hv2v3.ERROR_RECAPTCHAV2_AUDIO_EXCEPTION)
            ERROR_CONNECTION_RECAPTCHAV2_AUDIO = int(ERROR_CONNECTION_RECAPTCHAV2_AUDIO) + int(stat_hv2v3.ERROR_CONNECTION_RECAPTCHAV2_AUDIO)
            ABORT_TIMEOUT_RECAPTCHAV2_AUDIO = int(ABORT_TIMEOUT_RECAPTCHAV2_AUDIO) + int(stat_hv2v3.ABORT_TIMEOUT_RECAPTCHAV2_AUDIO)
            EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_AUDIO = int(EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_AUDIO) + int(stat_hv2v3.EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_AUDIO)

            RECAPTCHAV2_IMAGE_CHALLENGE = int(RECAPTCHAV2_IMAGE_CHALLENGE) + int(stat_hv2v3.RECAPTCHAV2_IMAGE_CHALLENGE)
            TRYS_RECAPTCHAV2_IMAGE_CHALLENGE = int(TRYS_RECAPTCHAV2_IMAGE_CHALLENGE) + int(stat_hv2v3.TRYS_RECAPTCHAV2_IMAGE_CHALLENGE)
            TRY1_RECAPTCHAV2_IMAGE_CHALLENGE = int(TRY1_RECAPTCHAV2_IMAGE_CHALLENGE) + int(stat_hv2v3.TRY1_RECAPTCHAV2_IMAGE_CHALLENGE)
            TRY2_RECAPTCHAV2_IMAGE_CHALLENGE = int(TRY2_RECAPTCHAV2_IMAGE_CHALLENGE) + int(stat_hv2v3.TRY2_RECAPTCHAV2_IMAGE_CHALLENGE)
            TRY3_RECAPTCHAV2_IMAGE_CHALLENGE = int(TRY3_RECAPTCHAV2_IMAGE_CHALLENGE) + int(stat_hv2v3.TRY3_RECAPTCHAV2_IMAGE_CHALLENGE)
            SUCCESS_RECAPTCHAV2_IMAGE_CHALLENGE = int(SUCCESS_RECAPTCHAV2_IMAGE_CHALLENGE) + int(stat_hv2v3.SUCCESS_RECAPTCHAV2_IMAGE_CHALLENGE)
            ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_CAP_SOLVER = int(ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_CAP_SOLVER) + int(stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_CAP_SOLVER)
            ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_NOT_FOUND = int(ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_NOT_FOUND) + int(stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_NOT_FOUND)
            ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_RATE_LIMIT = int(ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_RATE_LIMIT) + int(stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_RATE_LIMIT)
            ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_SOLVE = int(ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_SOLVE) + int(stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_SOLVE)
            ERROR_RECAPTCHAV2_IMAGE_CHALLENGE = int(ERROR_RECAPTCHAV2_IMAGE_CHALLENGE) + int(stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE)
            ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_EXCEPTION = int(ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_EXCEPTION) + int(stat_hv2v3.ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_EXCEPTION)
            ERROR_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE = int(ERROR_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE) + int(stat_hv2v3.ERROR_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE)
            ABORT_TIMEOUT_RECAPTCHAV2_IMAGE_CHALLENGE = int(ABORT_TIMEOUT_RECAPTCHAV2_IMAGE_CHALLENGE) + int(stat_hv2v3.ABORT_TIMEOUT_RECAPTCHAV2_IMAGE_CHALLENGE)
            EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_IMAGE_CHALLENGE = int(EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_IMAGE_CHALLENGE) + int(stat_hv2v3.EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_IMAGE_CHALLENGE)

            RECAPTCHAV3 = int(RECAPTCHAV3) + int(stat_hv2v3.RECAPTCHAV3)
            TRYS_RECAPTCHAV3 = int(TRYS_RECAPTCHAV3) + int(stat_hv2v3.TRYS_RECAPTCHAV3)
            TRY1_RECAPTCHAV3 = int(TRY1_RECAPTCHAV3) + int(stat_hv2v3.TRY1_RECAPTCHAV3)
            TRY2_RECAPTCHAV3 = int(TRY2_RECAPTCHAV3) + int(stat_hv2v3.TRY2_RECAPTCHAV3)
            TRY3_RECAPTCHAV3 = int(TRY3_RECAPTCHAV3) + int(stat_hv2v3.TRY3_RECAPTCHAV3)
            SUCCESS_RECAPTCHAV3 = int(SUCCESS_RECAPTCHAV3) + int(stat_hv2v3.SUCCESS_RECAPTCHAV3)
            ERROR_RECAPTCHAV3_NOT_FOUND = int(ERROR_RECAPTCHAV3_NOT_FOUND) + int(stat_hv2v3.ERROR_RECAPTCHAV3_NOT_FOUND)
            ERROR_RECAPTCHAV3_RATE_LIMIT = int(ERROR_RECAPTCHAV3_RATE_LIMIT) + int(stat_hv2v3.ERROR_RECAPTCHAV3_RATE_LIMIT)
            ERROR_RECAPTCHAV3_SOLVE = int(ERROR_RECAPTCHAV3_SOLVE) + int(stat_hv2v3.ERROR_RECAPTCHAV3_SOLVE)
            ERROR_RECAPTCHAV3 = int(ERROR_RECAPTCHAV3) + int(stat_hv2v3.ERROR_RECAPTCHAV3)
            ERROR_RECAPTCHAV3_EXCEPTION = int(ERROR_RECAPTCHAV3_EXCEPTION) + int(stat_hv2v3.ERROR_RECAPTCHAV3_EXCEPTION)
            ERROR_CONNECTION_RECAPTCHAV3 = int(ERROR_CONNECTION_RECAPTCHAV3) + int(stat_hv2v3.ERROR_CONNECTION_RECAPTCHAV3)
            ABORT_TIMEOUT_RECAPTCHAV3 = int(ABORT_TIMEOUT_RECAPTCHAV3) + int(stat_hv2v3.ABORT_TIMEOUT_RECAPTCHAV3)
            EXCEPTION_LOOP_SOLVING_RECAPTCHAV3 = int(EXCEPTION_LOOP_SOLVING_RECAPTCHAV3) + int(stat_hv2v3.EXCEPTION_LOOP_SOLVING_RECAPTCHAV3)

            HCAPTCHA = int(HCAPTCHA) + int(stat_hv2v3.HCAPTCHA)
            TRYS_HCAPTCHA = int(TRYS_HCAPTCHA) + int(stat_hv2v3.TRYS_HCAPTCHA)
            TRY1_HCAPTCHA = int(TRY1_HCAPTCHA) + int(stat_hv2v3.TRY1_HCAPTCHA)
            TRY2_HCAPTCHA = int(TRY2_HCAPTCHA) + int(stat_hv2v3.TRY2_HCAPTCHA)
            TRY3_HCAPTCHA = int(TRY3_HCAPTCHA) + int(stat_hv2v3.TRY3_HCAPTCHA)
            SUCCESS_HCAPTCHA = int(SUCCESS_HCAPTCHA) + int(stat_hv2v3.SUCCESS_HCAPTCHA)
            ERROR_CONNECTION_HCAPTCHA = int(ERROR_CONNECTION_HCAPTCHA) + int(stat_hv2v3.ERROR_CONNECTION_HCAPTCHA)
            ABORT_TIMEOUT_HCAPTCHA = int(ABORT_TIMEOUT_HCAPTCHA) + int(stat_hv2v3.ABORT_TIMEOUT_HCAPTCHA)
            EXCEPTION_LOOP_SOLVING_HCAPTCHA = int(EXCEPTION_LOOP_SOLVING_HCAPTCHA) + int(stat_hv2v3.EXCEPTION_LOOP_SOLVING_HCAPTCHA)

            with open(filename_stat_temp, 'w') as file:
                file.write(f'{RECAPTCHAV2_AUDIO}\n')
                file.write(f'{TRYS_RECAPTCHAV2_AUDIO}\n')
                file.write(f'{TRY1_RECAPTCHAV2_AUDIO}\n')
                file.write(f'{TRY2_RECAPTCHAV2_AUDIO}\n')
                file.write(f'{TRY3_RECAPTCHAV2_AUDIO}\n')
                file.write(f'{SUCCESS_RECAPTCHAV2_AUDIO}\n')
                file.write(f'{ERROR_RECAPTCHAV2_AUDIO_NOT_FOUND}\n')
                file.write(f'{ERROR_RECAPTCHAV2_AUDIO_RATE_LIMIT}\n')
                file.write(f'{ERROR_RECAPTCHAV2_AUDIO_SOLVE}\n')
                file.write(f'{ERROR_RECAPTCHAV2_AUDIO}\n')
                file.write(f'{ERROR_RECAPTCHAV2_AUDIO_EXCEPTION}\n')
                file.write(f'{ERROR_CONNECTION_RECAPTCHAV2_AUDIO}\n')
                file.write(f'{ABORT_TIMEOUT_RECAPTCHAV2_AUDIO}\n')
                file.write(f'{EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_AUDIO}\n')

                file.write(f'{RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                file.write(f'{TRYS_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                file.write(f'{TRY1_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                file.write(f'{TRY2_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                file.write(f'{TRY3_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                file.write(f'{SUCCESS_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                file.write(f'{ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_CAP_SOLVER}\n')
                file.write(f'{ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_NOT_FOUND}\n')
                file.write(f'{ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_RATE_LIMIT}\n')
                file.write(f'{ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_SOLVE}\n')
                file.write(f'{ERROR_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                file.write(f'{ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_EXCEPTION}\n')
                file.write(f'{ERROR_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                file.write(f'{ABORT_TIMEOUT_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                file.write(f'{EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_IMAGE_CHALLENGE}\n')

                file.write(f'{RECAPTCHAV3}\n')
                file.write(f'{TRYS_RECAPTCHAV3}\n')
                file.write(f'{TRY1_RECAPTCHAV3}\n')
                file.write(f'{TRY2_RECAPTCHAV3}\n')
                file.write(f'{TRY3_RECAPTCHAV3}\n')
                file.write(f'{SUCCESS_RECAPTCHAV3}\n')
                file.write(f'{ERROR_RECAPTCHAV3_NOT_FOUND}\n')
                file.write(f'{ERROR_RECAPTCHAV3_RATE_LIMIT}\n')
                file.write(f'{ERROR_RECAPTCHAV3_SOLVE}\n')
                file.write(f'{ERROR_RECAPTCHAV3}\n')
                file.write(f'{ERROR_RECAPTCHAV3_EXCEPTION}\n')
                file.write(f'{ERROR_CONNECTION_RECAPTCHAV3}\n')
                file.write(f'{ABORT_TIMEOUT_RECAPTCHAV3}\n')
                file.write(f'{EXCEPTION_LOOP_SOLVING_RECAPTCHAV3}\n')

                file.write(f'{HCAPTCHA}\n')
                file.write(f'{TRYS_HCAPTCHA}\n')
                file.write(f'{TRY1_HCAPTCHA}\n')
                file.write(f'{TRY2_HCAPTCHA}\n')
                file.write(f'{TRY3_HCAPTCHA}\n')
                file.write(f'{SUCCESS_HCAPTCHA}\n')
                file.write(f'{ERROR_CONNECTION_HCAPTCHA}\n')
                file.write(f'{ABORT_TIMEOUT_HCAPTCHA}\n')
                file.write(f'{EXCEPTION_LOOP_SOLVING_HCAPTCHA}\n')
                file.close()

            if is_providing_stat_v2a:
                with open(filename_stat_v2a, 'w') as file:
                    file.write('######################################################################################################################\n')
                    file.write('### STATS RECAPTCHA V2 (AUDIO)\n')
                    file.write('######################################################################################################################\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' RECAPTCHAV2_AUDIO                             : {RECAPTCHAV2_AUDIO}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRYS_RECAPTCHAV2_AUDIO                        : {TRYS_RECAPTCHAV2_AUDIO}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRY1_RECAPTCHAV2_AUDIO                        : {TRY1_RECAPTCHAV2_AUDIO}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRY2_RECAPTCHAV2_AUDIO                        : {TRY2_RECAPTCHAV2_AUDIO}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRY3_RECAPTCHAV2_AUDIO                        : {TRY3_RECAPTCHAV2_AUDIO}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' SUCCESS_RECAPTCHAV2_AUDIO                     : {SUCCESS_RECAPTCHAV2_AUDIO}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV2_AUDIO_NOT_FOUND             : {ERROR_RECAPTCHAV2_AUDIO_NOT_FOUND}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV2_AUDIO_RATE_LIMIT            : {ERROR_RECAPTCHAV2_AUDIO_RATE_LIMIT}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV2_AUDIO_SOLVE                 : {ERROR_RECAPTCHAV2_AUDIO_SOLVE}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV2_AUDIO                       : {ERROR_RECAPTCHAV2_AUDIO}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV2_AUDIO_EXCEPTION             : {ERROR_RECAPTCHAV2_AUDIO_EXCEPTION}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_CONNECTION_RECAPTCHAV2_AUDIO            : {ERROR_CONNECTION_RECAPTCHAV2_AUDIO}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ABORT_TIMEOUT_RECAPTCHAV2_AUDIO               : {ABORT_TIMEOUT_RECAPTCHAV2_AUDIO}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_AUDIO      : {EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_AUDIO}\n')
                    file.write('######################################################################################################################\n')
                    file.close()

            if is_providing_stat_v2ic:
                with open(filename_stat_v2ic, 'w') as file:
                    file.write('######################################################################################################################\n')
                    file.write('### STATS RECAPTCHA V2 (IMAGE CHALLENGE)\n')
                    file.write('######################################################################################################################\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' RECAPTCHAV2_IMAGE_CHALLENGE                             : {RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRYS_RECAPTCHAV2_IMAGE_CHALLENGE                        : {TRYS_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRY1_RECAPTCHAV2_IMAGE_CHALLENGE                        : {TRY1_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRY2_RECAPTCHAV2_IMAGE_CHALLENGE                        : {TRY2_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRY3_RECAPTCHAV2_IMAGE_CHALLENGE                        : {TRY3_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' SUCCESS_RECAPTCHAV2_IMAGE_CHALLENGE                     : {SUCCESS_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_CAP_SOLVER            : {ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_CAP_SOLVER}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_NOT_FOUND             : {ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_NOT_FOUND}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_RATE_LIMIT            : {ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_RATE_LIMIT}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_SOLVE                 : {ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_SOLVE}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV2_IMAGE_CHALLENGE                       : {ERROR_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_EXCEPTION             : {ERROR_RECAPTCHAV2_IMAGE_CHALLENGE_EXCEPTION}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE            : {ERROR_CONNECTION_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ABORT_TIMEOUT_RECAPTCHAV2_IMAGE_CHALLENGE               : {ABORT_TIMEOUT_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_IMAGE_CHALLENGE      : {EXCEPTION_LOOP_SOLVING_RECAPTCHAV2_IMAGE_CHALLENGE}\n')
                    file.write('######################################################################################################################\n')
                    file.close()

            if is_providing_stat_v3:
                with open(filename_stat_v3, 'w') as file:
                    file.write('######################################################################################################################\n')
                    file.write('### STATS RECAPTCHA V3\n')
                    file.write('######################################################################################################################\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' RECAPTCHAV3                             : {RECAPTCHAV3}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRYS_RECAPTCHAV3                        : {TRYS_RECAPTCHAV3}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRY1_RECAPTCHAV3                        : {TRY1_RECAPTCHAV3}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRY2_RECAPTCHAV3                        : {TRY2_RECAPTCHAV3}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRY3_RECAPTCHAV3                        : {TRY3_RECAPTCHAV3}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' SUCCESS_RECAPTCHAV3                     : {SUCCESS_RECAPTCHAV3}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV3_NOT_FOUND             : {ERROR_RECAPTCHAV3_NOT_FOUND}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV3_RATE_LIMIT            : {ERROR_RECAPTCHAV3_RATE_LIMIT}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV3_SOLVE                 : {ERROR_RECAPTCHAV3_SOLVE}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV3                       : {ERROR_RECAPTCHAV3}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_RECAPTCHAV3_EXCEPTION             : {ERROR_RECAPTCHAV3_EXCEPTION}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_CONNECTION_RECAPTCHAV3            : {ERROR_CONNECTION_RECAPTCHAV3}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ABORT_TIMEOUT_RECAPTCHAV3               : {ABORT_TIMEOUT_RECAPTCHAV3}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' EXCEPTION_LOOP_SOLVING_RECAPTCHAV3      : {EXCEPTION_LOOP_SOLVING_RECAPTCHAV3}\n')
                    file.write('######################################################################################################################\n')
                    file.close()
                            
            if is_providing_stat_h:
                with open(filename_stat_h, 'w') as file:
                    file.write('######################################################################################################################\n')
                    file.write('### STATS HCAPTCHA\n')
                    file.write('######################################################################################################################\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' HCAPTCHA                             : {HCAPTCHA}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRYS_HCAPTCHA                        : {TRYS_HCAPTCHA}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRY1_HCAPTCHA                        : {TRY1_HCAPTCHA}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRY2_HCAPTCHA                        : {TRY2_HCAPTCHA}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' TRY3_HCAPTCHA                        : {TRY3_HCAPTCHA}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' SUCCESS_HCAPTCHA                     : {SUCCESS_HCAPTCHA}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ERROR_CONNECTION_HCAPTCHA            : {ERROR_CONNECTION_HCAPTCHA}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' ABORT_TIMEOUT_HCAPTCHA               : {ABORT_TIMEOUT_HCAPTCHA}\n')
                    file.write('### ' + datetime.now().strftime('%d-%b-%Y-%H:%M:%S') + f' EXCEPTION_LOOP_SOLVING_HCAPTCHA      : {EXCEPTION_LOOP_SOLVING_HCAPTCHA}\n')
                    file.write('######################################################################################################################\n')
                    file.close()

            sleep(1)
            q_stat.task_done()

############################################################################
# Main
############################################################################

if __name__ == '__main__':
    import uvicorn
	
    uvicorn.run(app, host="0.0.0.0", port=8000)

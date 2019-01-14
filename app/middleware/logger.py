import os, time, logging
from app.common.config import cfg
from app.common.utils import project_path, make_dir

log_folder = os.path.join(project_path, 'logs')
log_format_filename = cfg.get('logger.format_filename')
log_format_msg = cfg.get('logger.format_msg')
log_format_time = cfg.get('logger.format_time')
log_level = cfg.get('logger.log_level')


def logger(app):
    make_dir(log_folder)
    filename = time.strftime(log_format_filename, time.localtime(time.time())) + '.log'
    handler = logging.FileHandler(os.path.join(log_folder, filename), encoding='UTF-8')
    log_format = logging.Formatter(log_format_msg, log_format_time)
    handler.setFormatter(log_format)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

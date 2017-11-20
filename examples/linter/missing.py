def process_stuff(params):
    executed = False
    if not params:
        raise ValueError('empty command list')
        for foo in params:
            foo.execute
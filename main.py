import asyncio, telnetlib3

async def repl(r, w):
    params = {
    '*IDN' : 'fake scpi,SN 123DEADBEEF,v0.0.1',
    'SARA' : '1000',
    'NS'   : '512',
    'CHAN' : '33,35',
    'TRSE' : '3000 -',
    'SET50' : '',
    'ARM'  : '',
    'STOP' : '',
    'SAST' : 'TRIG',
    'DATA' : '1,2,3,4,5,6,7,8,9,10',
    }


    while True:
        try:
            cmd = await r.readline()
            cmd = cmd.strip().upper()
            w.echo(cmd + '\r\n')
            cmd,_,args = cmd.partition(' ')
            cmd,q,_ = cmd.partition('?')
            if cmd not in params:
                w.write(f'Unknown command {cmd}\r\n')
            elif q != '':
                w.write(f'{params[cmd]}\r\n')
            else:
                params[cmd] = args
            await w.drain()
        except:
            w.close()
            break

loop = asyncio.get_event_loop()
coro = telnetlib3.create_server(port=5025, shell=repl)
server = loop.run_until_complete(coro)
loop.run_until_complete(server.wait_closed())

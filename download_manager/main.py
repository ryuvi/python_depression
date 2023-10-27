import click as c
import requests as req
import threading as thd

# This function is used for each chunk of file handled
# by each thread for downloading the content from specified
# location to storage
def Handler(start, end, url, filename):
    # specify the starting and ending of the file
    headers = {'Range': 'bytes=%d-%d' % (start, end)}
    # request the specified part and get into variable
    r = req.get(url, headers=headers, stream=True)
    #open the file and write the content of the html page
    # into file.
    with open(filename, 'r+b') as fp:
        fp.seek(start)
        var = fp.tell()
        fp.write(r.content)

@c.command(help="It downloads the specified file with specified name")
@c.option('--number_of_threads', default=4, help='No of Threads')
@c.option('--name', type=c.Path(), help='Name of the file with extension')
@c.argument('url_of_file',type=c.Path())
@c.pass_context
def download_file(ctx,url_of_file,name,number_of_threads):
    r = req.head(url_of_file)
    if name:
        file_name = name
    else:
        file_name = url_of_file.split('/')[-1]
    try:
        file_size = int(r.headers['content-length'])
    except:
        print('Invalid URL')
        return -1
    part = int(file_size) / number_of_threads
    fp = open(file_name, 'wb')
    fp.write('\0' * file_size)
    fp.close()

    for threads in range(number_of_threads):
        start = part * threads
        end = start + part
        
        t = thd.Thread(target=Handler,
                       kwargs={'start': start, 'end': end, 'url': url_of_file, 'filename': file_name})
        t.setDaemon(True)
        t.start()

    main_thread = thd.current_thread()
    for t in thd.enumerate():
        if t is main_thread:
            continue
        t.join
    print('%s downloaded' % file_name)


if __name__ == '__main__':
    download_file(obj={})


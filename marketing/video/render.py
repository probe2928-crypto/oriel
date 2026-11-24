import sys, subprocess
from playwright.sync_api import sync_playwright
w,h,out=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]; fps=30
ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(fps),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':w,'height':h})
    pg.goto('http://localhost:8766/film.html'); pg.wait_for_function('window.ready===true'); pg.wait_for_timeout(800)
    n=int(pg.evaluate('DUR')*fps)
    for i in range(n):
        pg.evaluate(f'render({i/fps})'); ff.stdin.write(pg.screenshot(type='jpeg',quality=92))
    b.close()
ff.stdin.close(); ff.wait(); print('done',out,n)

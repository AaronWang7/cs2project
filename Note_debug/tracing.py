#Aaron Wang, Tracing Notes


#what is tracing?
# Lets you se. debugging method that lets you see what is happening with your function
#Python -m trace --count C:\Users\aaron.wang\Documents\cs2project\Note_debug\traing.py
#Python -m trace --trace C:\Users\aaron.wang\Documents\cs2project\Note_debug\traing.py
#Python -m trace --listfunctions C:\Users\aaron.wang\Documents\cs2project\Note_debug\traing.py
"""
--trace (displays function lines as theu are executed)
-- count (displays the number of times each function is executed)
trackcalls (display the relationship between the functions)
listfunctions(displays rthe functions in the project)
"""
import trace
import sys
import trace
trecer = trace.Trace(count=False,trace=True)
def trace_calls(frame,event,arg):
    if event == 'call':
        print(f"calling function:{frame.f_code.co_name}")
    elif event == 'line':
        print(f'executing line:{frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return':
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception':
        print(f'exception in {frame.f_code.co_name}: {arg}')
        return trace_calls
sys.settrace(trace_calls)

"""
Events types:
call - when the function is called
line - when a new line is executed
return - when the function returns a vaule
exception - when there is an excepyion raised
"""

#what are some ways we can debug by tracing?
    # make a function that lets us see how our functions are interacting and running
#how do you access the debugger in VS Code?
    #F5
#what is testing?
    # Mkae sure there no bug, going through the code trying to break it, have testers be not the person who wrote the code
#what are boundary conditions?
    #Your outliers that are not likly to caused problems, User conditions that are strange and/or likliy to cause issue, extream highs and lows
#how do you handle when users give strange inputs?
    #Try expect

trecer = trace.Trace(count=False,trace=True)

def add(numone,numtwo):
    return numone + numtwo




def sub(numone,numtwo):
    return numone - numtwo
print(sub(1,56))
print(add(1,56))

trecer.run('sub(1,56)')

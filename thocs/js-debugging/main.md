Debugging Javascript code
====================================================================
> Tools for debugging Javascript code as simple as possible. As always the 
approach first is to attach the default cli debugging client to the debuggee
target. Before to continue is important to note that Browser Javascript is
diferent from Node Javascript. With the later you have a different mechanism
for imports. In this guide we will talk only about Node Javascript. 


Installing
====================================================================
The basic tools needed are:

- Node runtime
- Firefox webbrowser
- VSCode


Starting the debugging session
====================================================================

Run your code in debugging mode
---------------------------------
As with many other languages, you need to execute your code in debugging 
mode. To do this call your script with:

    node --inspect-brk <your-code>

This will wait for a client to connect and then stop the execution at 
the script first's statement [1](). Note that this option is also available in 
`jdb`, `gdb`.

The previous actions implies the following defaults:

    - host: localhost or 127.0.0.1
    - port: 9229

Connect your debugging client
---------------------------------
There are several debugging clients for JS.

### Default CLI Client
Node runtime comes with a non full featured cli debugging client. You can
call it with `node inspect <host>:<port>`. As we will work in local just
call it with the defaults `node inspect 127.0.0.1:9229`.

### Google Chrome
Node is based in the same Google Chrome Javascript V8 Javascript interpreter.
All Chrome web browsers have native support for debugging Javascript applications.
What about Mozilla Firefox? Because Firefox uses _SpiderMonkey_ engine there is no
way to attach Firefox debugging tools to the their Javascript Engine. To launch
the Chrome debugger just type in the omni bar `chrome://inspect`.

### VSCode
VSCode is made on top of Chrome (well Chromium). This means that by default the
editor is a full featured debugging client. You can attach this debugging client
by generating a default `launch.json` file in the `Debug` activity on the side 
bar.
You only need to remove the `program` attribute from this config, and change
the value of `request` to `attach`.


Additional Notes
====================================================================

About the import system
---------------------------------
`require` is not a reserved word [3]. The import style influences the file 
extension: `cjs` for _CommonJS_ `require()` imports and `m̀js` for _ECMAScript_
`export` exports [4].


Tracking log
====================================================================
### 250529
File created. 

References
====================================================================
[1]: https://nodejs.org/en/learn/getting-started/debugging#command-line-options 
[2]: https://262.ecma-international.org/15.0/index.html#sec-debugger-statement
[3]: https://262.ecma-international.org/15.0/index.html#prod-ReservedWord
[4]: https://nodejs.org/api/esm.html#require

#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
#include <syslog.h>
#include <string.h>
#include <syslog.h> // info logging

// headers from the glibc for daemons

int main(void){
    // process and session ideas
    pid_t pid, sid;

    // need to create a child process
    pid = fork();
    if (pid < 0){
        exit(EXIT_FAILURE);
    }
    
    // Exit parent process if pid is good
    if(pid > 0){
        exit(EXIT_SUCCESS);
    }
    umask(0); // get full access to files made by the daemon

    //Create a sid for the child
    sid = setsid();
    if (sid < 0){
        printf("Could not create system id for subprocess\n");
        exit(EXIT_FAILURE);
    }


    if((chdir("/")) < 0){
        printf("Could not change daemon to root directory.\n");
        exit(EXIT_FAILURE);
    }
    /* Close out the standard file descriptors */
    // daemons cannot use the terminal
    // and using constants make teh code portable

    // need to make sys logs very verbose, for debugging purposes.
    //setlogmask (LOG_UPTO (LOG_NOTICE));
    // need to start up rsyslog for log to work

    openlog("system_log", LOG_CONS | LOG_PID, LOG_USER);
    syslog(LOG_INFO, "Starting daemon log.");
    close(STDIN_FILENO);
    close(STDOUT_FILENO);
    close(STDERR_FILENO);
    while(1){
        syslog(LOG_INFO, "Program UID %d", getuid());
        sleep(30); // wait 30 seconds
        
        exit(1); // while testing
    }
    closelog();
    exit(EXIT_FAILURE);
}
#include <stdlib.h>
#include <stdarg.h>
#include "umberlog.h"

int
main(
    int    argc,
    char * argv[]
    )
{
	int log_flags = 0;

	log_flags |= LOG_PERROR;
	ul_openlog("", log_flags, LOG_USER);

	ul_syslog(4, "[umberlog test] testing ... %s\n", "1, 2, 3",
		"count", "%s", "2",
		"el.0.type",  "%s", "ladybug",
		"el.0.name",  "%s", "natalie",
		"el.0.spots", "%s", "12",
		"el.1.type",  "%s", "ant",
		"el.1.name",  "%s", "B289",
		"el.1.role",  "%s", "worker",
		"el.1.age",   "%s", "9",
		NULL);

	ul_closelog();

	return 0;
}


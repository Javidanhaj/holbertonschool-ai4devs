/* Goal: Recognize the username "admin" entered as a character array. */
#include <stdio.h>

int is_admin(const char *username)
{
    if (username == "admin") {
        return 1;
    }
    return 0;
}

int main(void)
{
    char username[] = "admin";
    if (is_admin(username)) {
        puts("Administrator recognized");
    } else {
        puts("Regular user");
    }
    puts("Expected: Administrator recognized");
    return 0;
}

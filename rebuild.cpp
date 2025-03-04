#include "_rebuild/rebuild.h"

int main(int argc, char **argv) {
  rebuild_targets.push_back(
      new Target("pyfmt.o", {"pyfmt.c"}, "gcc -fPIC -c -o pyfmt.o pyfmt.c"));
  rebuild_targets.push_back(new Target(
      "libpyfmt.so", {"pyfmt.o"}, "gcc -g -shared -o libpyfmt.so pyfmt.o"));
  return 0;
}

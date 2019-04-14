# Streaming with a socket
1. Open two terminals on the same midway 2 login host. In both terminals go to the current directory 
   `$HOME/Spark/labs/6` assuming that you did `git clone ...` from `$HOME`.
1. In one of the terminals randomly generate port number in the range from 9000 to 10000 to minimize the possibility of
   collision with other users and write the corresponding commands
   to `mync.sh` and `mystream.sh`
   ```
   make generate
   ```
2. In the first terminal:
   1. Set up the environment for netcat:
      ```
      source env.sh
      ```
   2. Run netcat:
      ```
      make nc
      ```
3. In the second terminal make sure to set up an environment for Spark and run Spark streaming program:
   ```
   source ../env.sh
   make word_count
   ```
4. Now type a line with words in the first (netcat) terminal and press `Enter`: look how the words are processed in the second terminal
5. Repeat. This time all (the old and the new) lines are reprocessed
6. Type `Ctrl+C` in netcat terminal to kill both servers

# Streaming with files

Open two terminals on the same host, current directory:
1. The first one runs Spark Streaming program that picks up new files from `input_csv` directory
   ```
   make age
   ```
2. In the second one move one file at a time from `tmp` to `input_csv` and observe 
   how they are processed in the first terminal
3. Notice it is important to use `mv` and not `cp`: files in `input_csv` are supposed to be immutable. `mv` works instantenously while
   something like `cp` might take time and as result Spark might notice part of the file and ignore the rest.
4. To kill the program, type `Ctrl+C` in the first terminal.
5. To clean output and restore `tmp` content, do
   ```
   make clean
   ```



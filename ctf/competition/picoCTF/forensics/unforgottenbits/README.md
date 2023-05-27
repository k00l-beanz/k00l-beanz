# Mount the filesystem
```
$ sudo losetup -P /dev/loop0 disk.flag.img
$ lsblk /dev/loop0
NAME      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0       7:0    0    1G  0 loop 
├─loop0p1 259:0    0  100M  0 part 
├─loop0p2 259:1    0  256M  0 part 
└─loop0p3 259:2    0  667M  0 part /mnt/unforgottenbits
$ sudo mount /dev/loop0p3 /mnt/unforgottenbits 
```
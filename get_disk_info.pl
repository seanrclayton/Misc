#!/usr/bin/perl
use strict; 
use warnings; 
use Filesys::Df;
use Getopt::Long qw(GetOptions);
use Data::Dumper;

# a little ruby  syntax to keep me sane
sub puts {print @_, "\n"}

my $file_system;

GetOptions('f=s' => \$file_system) or die "Usage: $0  -f filesystem";

my $disk_info =  df($file_system);

# Reminder of how to print contents of this hash puts Dumper($disk_info);

my $percent_used = $disk_info -> {per};

 puts  $percent_used . " percent used " .  "#"  x ($percent_used / 5) ;

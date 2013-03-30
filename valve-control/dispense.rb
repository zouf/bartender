#!/usr/bin/env ruby

# Usage: dispense [valve number] [number of ounces]

valve_number = ARGV.first.to_i
num_ounces = ARGV.last.to_f

VALVE2PORT = {
    1 => 1,
    2 => 0,
    3 => 10,
    4 => 11,
    5 => 13,
    6 => 7,
    7 => 6,
    8 => 5,
    9 => 4,
    10 => 3 
  }

# Make sure all valves are OUTPUT
VALVE2PORT.each_pair do |valve,port|
  system "gpio mode #{port} out"
end


port_number = VALVE2PORT[ valve_number ]
dead_reckoning = 12.5 * num_ounces

$stderr.puts "Valve #{valve_number} => #{port_number}"
$stderr.puts "#{num_ounces} => #{dead_reckoning} seconds"

system "gpio write #{port_number} 1"
sleep dead_reckoning
system "gpio write #{port_number} 0"

system "./activate-the-vibrator.sh"

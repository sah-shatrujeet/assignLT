output "instance_id" {
  description    =  "List of instances id"
  value          =  aws_instance.ec2.*.id
}

output "private_ip" {
  description    =  "List of private IP addresses assigned to the instances"
  value          =  aws_instance.ec2.*.private_ip
}

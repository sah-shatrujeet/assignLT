resource "aws_instance" "ec2" {
  count                          =  length(var.ec2)
  ami                            =  var.ec2[count.index].ami_id
  instance_type                  =  var.ec2[count.index].instance_type
  key_name                       =  var.ec2[count.index].key_name
  subnet_id                      =  var.ec2[count.index].subnet
  vpc_security_group_ids         =  var.ec2[count.index].security_groups

  tags                           =  merge(
    {
      Provisioner                =  "Terraform"
    },
    var.tags
  )
}

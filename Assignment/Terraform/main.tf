resource "aws_ami_from_instance" "webapp" {
  name               = "webapp-ami"
  source_instance_id = "i-0bea2fa30c69a9bc0"
}


resource "aws_launch_configuration" "webapp" {
  name = "webapp-launch-config"
  image_id = "ami-07ce932e46dc1e621"
  instance_type = "t2.micro"
  security_groups = ["sg-0fa08c0a8928303b6"]
}

resource "aws_autoscaling_group" "webapp" {
  desired_capacity = 0
  max_size = 0
  min_size = 0
  health_check_grace_period = 300
  health_check_type = "EC2"
  force_delete = true
  launch_configuration = aws_launch_configuration.webapp.id
  vpc_zone_identifier = ["subnet-03b5ce904debe5fa3"]
}
